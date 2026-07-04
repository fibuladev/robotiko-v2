#!/usr/bin/env node

/**
 * OAuth2 Authentication Helper for Robotiko Google Drive MCP
 *
 * Run this ONCE to authenticate:
 *   npm run auth
 *
 * This opens a browser, you log in with the fibuladev Google account,
 * grant permissions, and the token is saved locally.
 */

import { google } from 'googleapis';
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join } from 'path';
import { createServer } from 'http';
import { exec } from 'child_process';
import { fileURLToPath } from 'url';
import { homedir } from 'os';

// Config paths
const CONFIG_DIR = join(homedir(), '.config', 'robotiko-mcp-gdrive');
const OAUTH_KEYS_PATH = process.env.GDRIVE_OAUTH_PATH || join(CONFIG_DIR, 'gcp-oauth.keys.json');
const TOKEN_PATH = process.env.GDRIVE_TOKEN_PATH || join(CONFIG_DIR, 'tokens.json');

// Scopes — only what we need for asset management
const SCOPES = [
  'https://www.googleapis.com/auth/drive.file',
];

/**
 * Load OAuth2 client from credentials file
 */
export function loadOAuthClient() {
  if (!existsSync(OAUTH_KEYS_PATH)) {
    throw new Error(
      `OAuth credentials not found at: ${OAUTH_KEYS_PATH}\n` +
      `Download from Google Cloud Console and place at that path.\n` +
      `Or set GDRIVE_OAUTH_PATH environment variable.`
    );
  }

  const keys = JSON.parse(readFileSync(OAUTH_KEYS_PATH, 'utf-8'));
  const { client_id, client_secret } = keys.installed || keys.web;

  return new google.auth.OAuth2(client_id, client_secret, 'http://localhost:3199/callback');
}

/**
 * Get authenticated client (loads saved token or runs auth flow)
 */
export async function getAuthenticatedClient() {
  const oauth2Client = loadOAuthClient();

  // Try loading saved token
  if (existsSync(TOKEN_PATH)) {
    const tokens = JSON.parse(readFileSync(TOKEN_PATH, 'utf-8'));
    oauth2Client.setCredentials(tokens);

    // Check if token needs refresh
    if (tokens.expiry_date && tokens.expiry_date < Date.now()) {
      try {
        const { credentials } = await oauth2Client.refreshAccessToken();
        oauth2Client.setCredentials(credentials);
        saveToken(credentials);
      } catch (err) {
        console.error('Token refresh failed. Re-run: npm run auth');
        throw err;
      }
    }

    return oauth2Client;
  }

  throw new Error(
    'No saved token found. Run authentication first:\n' +
    '  cd _tools/mcp-gdrive && npm run auth'
  );
}

/**
 * Save token to disk
 */
function saveToken(tokens) {
  if (!existsSync(CONFIG_DIR)) {
    mkdirSync(CONFIG_DIR, { recursive: true });
  }
  writeFileSync(TOKEN_PATH, JSON.stringify(tokens, null, 2));
}

/**
 * Interactive auth flow — run once to get token
 */
async function runAuthFlow() {
  console.log('=== Robotiko Google Drive MCP — Authentication ===\n');

  const oauth2Client = loadOAuthClient();

  const authUrl = oauth2Client.generateAuthUrl({
    access_type: 'offline',
    scope: SCOPES,
    prompt: 'consent',
  });

  console.log('Open this URL in your browser:\n');
  console.log(authUrl);
  console.log('\nWaiting for callback on http://localhost:3199/callback ...\n');

  // Start local server to receive OAuth callback
  const code = await new Promise((resolve, reject) => {
    const server = createServer((req, res) => {
      const url = new URL(req.url, 'http://localhost:3199');
      const authCode = url.searchParams.get('code');

      if (authCode) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end('<h1>Authentication successful!</h1><p>You can close this tab and return to the terminal.</p>');
        server.close();
        resolve(authCode);
      } else {
        res.writeHead(400, { 'Content-Type': 'text/html' });
        res.end('<h1>Authentication failed</h1><p>No code received.</p>');
        server.close();
        reject(new Error('No auth code received'));
      }
    });

    server.listen(3199, () => {
      // Try to open browser automatically
      exec(`start "" "${authUrl}"`, (err) => {
        if (err) console.log('Could not open browser automatically. Please open the URL above manually.');
      });
    });

    // Timeout after 2 minutes
    setTimeout(() => {
      server.close();
      reject(new Error('Authentication timed out (2 minutes)'));
    }, 120000);
  });

  // Exchange code for token
  const { tokens } = await oauth2Client.getToken(code);
  saveToken(tokens);

  console.log(`Token saved to: ${TOKEN_PATH}`);
  console.log('Authentication complete! MCP server is ready to use.\n');
}

// Run auth flow if this file is executed directly
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  runAuthFlow().catch((err) => {
    console.error('Authentication failed:', err.message);
    process.exit(1);
  });
}
