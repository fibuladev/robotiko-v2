#!/usr/bin/env node

/**
 * Robotiko Google Drive MCP Server
 *
 * A custom MCP server for managing binary assets (PNG, MP4, WAV)
 * on Google Drive. Built for the Robotiko v2.0 production pipeline.
 *
 * Tools:
 *   gdrive_list_folder  — Browse Drive folders
 *   gdrive_search       — Find files by name/type
 *   gdrive_create_folder — Create folders
 *   gdrive_upload        — Upload local files to Drive
 *   gdrive_move          — Move files between folders
 *
 * Usage:
 *   First authenticate: npm run auth
 *   Then run as MCP server: npm start
 */

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';

import { getAuthenticatedClient } from './auth.js';
import {
  listFolder,
  searchFiles,
  createFolder,
  uploadFile,
  moveFile,
  TOOL_DEFINITIONS,
} from './tools.js';

// Create MCP server
const server = new Server(
  {
    name: 'robotiko-gdrive',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Cached auth client
let authClient = null;

async function getAuth() {
  if (!authClient) {
    authClient = await getAuthenticatedClient();
  }
  return authClient;
}

// Register tool list handler
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return { tools: TOOL_DEFINITIONS };
});

// Register tool call handler
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    const auth = await getAuth();
    let result;

    switch (name) {
      case 'gdrive_list_folder':
        result = await listFolder(auth, args || {});
        break;

      case 'gdrive_search':
        result = await searchFiles(auth, args || {});
        break;

      case 'gdrive_create_folder':
        result = await createFolder(auth, args);
        break;

      case 'gdrive_upload':
        result = await uploadFile(auth, args);
        break;

      case 'gdrive_move':
        result = await moveFile(auth, args);
        break;

      default:
        return {
          content: [
            {
              type: 'text',
              text: `Unknown tool: ${name}`,
            },
          ],
          isError: true,
        };
    }

    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify(result, null, 2),
        },
      ],
    };
  } catch (error) {
    return {
      content: [
        {
          type: 'text',
          text: `Error: ${error.message}`,
        },
      ],
      isError: true,
    };
  }
});

// Start server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('Robotiko Google Drive MCP server running on stdio');
}

main().catch((err) => {
  console.error('Failed to start MCP server:', err);
  process.exit(1);
});
