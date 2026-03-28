/**
 * Google Drive Tool Implementations for Robotiko MCP
 *
 * 5 tools tailored for binary asset management:
 * - listFolder: Browse episode folders
 * - searchFiles: Find assets by name/type
 * - createFolder: Create episode folder structure on Drive
 * - uploadFile: Upload PNG/MP4/WAV assets
 * - moveFile: Organize files between folders
 */

import { google } from 'googleapis';
import { readFileSync } from 'fs';
import { basename, extname } from 'path';

/**
 * Get Drive API client
 */
function getDrive(auth) {
  return google.drive({ version: 'v3', auth });
}

/**
 * MIME type mapping for common asset types
 */
const MIME_TYPES = {
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.mp4': 'video/mp4',
  '.wav': 'audio/wav',
  '.mp3': 'audio/mpeg',
  '.md': 'text/markdown',
  '.json': 'application/json',
  '.txt': 'text/plain',
};

/**
 * Tool: listFolder
 * List contents of a Google Drive folder
 */
export async function listFolder(auth, { folderId, pageSize = 50, pageToken }) {
  const drive = getDrive(auth);

  const query = folderId
    ? `'${folderId}' in parents and trashed = false`
    : `'root' in parents and trashed = false`;

  const res = await drive.files.list({
    q: query,
    pageSize,
    pageToken,
    fields: 'nextPageToken, files(id, name, mimeType, size, modifiedTime, parents)',
    orderBy: 'name',
  });

  return {
    files: res.data.files.map((f) => ({
      id: f.id,
      name: f.name,
      type: f.mimeType === 'application/vnd.google-apps.folder' ? 'folder' : 'file',
      mimeType: f.mimeType,
      size: f.size ? `${(parseInt(f.size) / 1024 / 1024).toFixed(2)} MB` : null,
      modified: f.modifiedTime,
    })),
    nextPageToken: res.data.nextPageToken || null,
    total: res.data.files.length,
  };
}

/**
 * Tool: searchFiles
 * Search for files by name pattern or MIME type
 */
export async function searchFiles(auth, { query, mimeType, pageSize = 20 }) {
  const drive = getDrive(auth);

  const conditions = ['trashed = false'];
  if (query) conditions.push(`name contains '${query}'`);
  if (mimeType) conditions.push(`mimeType = '${mimeType}'`);

  const res = await drive.files.list({
    q: conditions.join(' and '),
    pageSize,
    fields: 'files(id, name, mimeType, size, modifiedTime, parents, webViewLink)',
    orderBy: 'modifiedTime desc',
  });

  return {
    results: res.data.files.map((f) => ({
      id: f.id,
      name: f.name,
      type: f.mimeType === 'application/vnd.google-apps.folder' ? 'folder' : 'file',
      mimeType: f.mimeType,
      size: f.size ? `${(parseInt(f.size) / 1024 / 1024).toFixed(2)} MB` : null,
      modified: f.modifiedTime,
      link: f.webViewLink,
    })),
    count: res.data.files.length,
  };
}

/**
 * Tool: createFolder
 * Create a folder (optionally inside a parent folder)
 */
export async function createFolder(auth, { name, parentFolderId }) {
  const drive = getDrive(auth);

  const fileMetadata = {
    name,
    mimeType: 'application/vnd.google-apps.folder',
  };

  if (parentFolderId) {
    fileMetadata.parents = [parentFolderId];
  }

  const res = await drive.files.create({
    resource: fileMetadata,
    fields: 'id, name, webViewLink',
  });

  return {
    id: res.data.id,
    name: res.data.name,
    link: res.data.webViewLink,
  };
}

/**
 * Tool: uploadFile
 * Upload a local file to Google Drive
 */
export async function uploadFile(auth, { localPath, folderId, fileName }) {
  const drive = getDrive(auth);

  const name = fileName || basename(localPath);
  const ext = extname(name).toLowerCase();
  const mimeType = MIME_TYPES[ext] || 'application/octet-stream';

  const fileMetadata = { name };
  if (folderId) {
    fileMetadata.parents = [folderId];
  }

  const { createReadStream } = await import('fs');

  const res = await drive.files.create({
    resource: fileMetadata,
    media: {
      mimeType,
      body: createReadStream(localPath),
    },
    fields: 'id, name, size, webViewLink',
  });

  return {
    id: res.data.id,
    name: res.data.name,
    size: res.data.size ? `${(parseInt(res.data.size) / 1024 / 1024).toFixed(2)} MB` : null,
    link: res.data.webViewLink,
  };
}

/**
 * Tool: moveFile
 * Move a file from one folder to another
 */
export async function moveFile(auth, { fileId, newParentFolderId }) {
  const drive = getDrive(auth);

  // Get current parents
  const file = await drive.files.get({
    fileId,
    fields: 'parents',
  });

  const previousParents = file.data.parents ? file.data.parents.join(',') : '';

  const res = await drive.files.update({
    fileId,
    addParents: newParentFolderId,
    removeParents: previousParents,
    fields: 'id, name, parents, webViewLink',
  });

  return {
    id: res.data.id,
    name: res.data.name,
    newParent: newParentFolderId,
    link: res.data.webViewLink,
  };
}

/**
 * Tool definitions for MCP registration
 */
export const TOOL_DEFINITIONS = [
  {
    name: 'gdrive_list_folder',
    description: 'List contents of a Google Drive folder. Returns files and subfolders with their IDs, names, types, and sizes.',
    inputSchema: {
      type: 'object',
      properties: {
        folderId: {
          type: 'string',
          description: 'Google Drive folder ID. Omit or leave empty to list root folder.',
        },
        pageSize: {
          type: 'number',
          description: 'Max results to return (default: 50, max: 100)',
        },
        pageToken: {
          type: 'string',
          description: 'Pagination token from previous request',
        },
      },
    },
  },
  {
    name: 'gdrive_search',
    description: 'Search for files in Google Drive by name or MIME type. Returns matching files with IDs, names, and links.',
    inputSchema: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'Search term to match against file names',
        },
        mimeType: {
          type: 'string',
          description: 'Filter by MIME type (e.g., "image/png", "video/mp4", "audio/wav")',
        },
        pageSize: {
          type: 'number',
          description: 'Max results to return (default: 20)',
        },
      },
    },
  },
  {
    name: 'gdrive_create_folder',
    description: 'Create a new folder in Google Drive. Optionally place it inside a parent folder.',
    inputSchema: {
      type: 'object',
      properties: {
        name: {
          type: 'string',
          description: 'Name for the new folder',
        },
        parentFolderId: {
          type: 'string',
          description: 'ID of the parent folder. Omit to create in root.',
        },
      },
      required: ['name'],
    },
  },
  {
    name: 'gdrive_upload',
    description: 'Upload a local file to Google Drive. Supports PNG, JPG, MP4, WAV, MD, JSON, and other common formats.',
    inputSchema: {
      type: 'object',
      properties: {
        localPath: {
          type: 'string',
          description: 'Absolute path to the local file to upload',
        },
        folderId: {
          type: 'string',
          description: 'Google Drive folder ID to upload into. Omit for root.',
        },
        fileName: {
          type: 'string',
          description: 'Override the file name on Drive. Defaults to local file name.',
        },
      },
      required: ['localPath'],
    },
  },
  {
    name: 'gdrive_move',
    description: 'Move a file or folder to a different parent folder in Google Drive.',
    inputSchema: {
      type: 'object',
      properties: {
        fileId: {
          type: 'string',
          description: 'Google Drive ID of the file/folder to move',
        },
        newParentFolderId: {
          type: 'string',
          description: 'Google Drive ID of the destination folder',
        },
      },
      required: ['fileId', 'newParentFolderId'],
    },
  },
];
