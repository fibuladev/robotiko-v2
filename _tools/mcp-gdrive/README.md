# Robotiko Google Drive MCP Server

Custom MCP server for managing binary assets (PNG, MP4, WAV) on Google Drive.
Built for the Robotiko v2.0 production pipeline.

## Why Custom?

We don't use third-party MCP packages. This server is ~300 lines of code with only two dependencies:
- `googleapis` — Google's official Node.js SDK
- `@modelcontextprotocol/sdk` — Official MCP protocol SDK

## Tools

| Tool | Description |
|---|---|
| `gdrive_list_folder` | Browse Drive folder contents |
| `gdrive_search` | Find files by name or MIME type |
| `gdrive_create_folder` | Create folders |
| `gdrive_upload` | Upload local files (PNG, MP4, WAV, etc.) |
| `gdrive_move` | Move files between folders |

## Setup

### Step 1: Google Cloud Console

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Sign in with the project Google account
3. Create a new project (e.g., `robotiko-v2`)
4. Enable the **Google Drive API**:
   - Go to APIs & Services → Library
   - Search "Google Drive API" → Enable
5. Configure OAuth consent screen:
   - Go to APIs & Services → OAuth consent screen
   - App name: `Robotiko Drive MCP`
   - User support email: your email
   - Audience: **External**
   - Add your email as a test user
6. Create OAuth credentials:
   - Go to APIs & Services → Credentials
   - Click **+ CREATE CREDENTIALS** → **OAuth client ID**
   - Application type: **Desktop app**
   - Name: `Robotiko MCP Client`
   - Click **Create** → **Download JSON**

### Step 2: Install

```bash
cd _tools/mcp-gdrive
npm install
```

### Step 3: Place Credentials

```bash
mkdir -p ~/.config/robotiko-mcp-gdrive
# Move the downloaded JSON file:
mv ~/Downloads/client_secret_*.json ~/.config/robotiko-mcp-gdrive/gcp-oauth.keys.json
```

### Step 4: Authenticate

```bash
npm run auth
```

This opens your browser. Sign in with the project Google account, grant permissions.
Token is saved to `~/.config/robotiko-mcp-gdrive/tokens.json`.

### Step 5: Configure Claude Code

Add a `.mcp.json` file in the **project root** (not inside `.claude/`):

```json
{
  "mcpServers": {
    "google-drive": {
      "command": "node",
      "args": ["_tools/mcp-gdrive/src/index.js"],
      "cwd": "_tools/mcp-gdrive"
    }
  }
}
```

> **Important:** Claude Code reads MCP server configs from `.mcp.json` at the project root.
> The `.claude/mcp.json` path does NOT work — tools will silently fail to load.

### Step 6: Test

Start a new Claude Code session. The Google Drive tools should appear automatically.
You can verify by checking the MCP servers panel in Claude Code (should show "Connected").

## Drive Folder Structure

```
robotiko-v2/
  ep01/
    raw/          ← Generated images (all variants)
    selected/     ← Curated best images
    audio/        ← WAV files
    video/        ← Final MP4 clips
  ep02/
    ...
```

## Environment Variables (Optional)

| Variable | Default | Description |
|---|---|---|
| `GDRIVE_OAUTH_PATH` | `~/.config/robotiko-mcp-gdrive/gcp-oauth.keys.json` | OAuth credentials file |
| `GDRIVE_TOKEN_PATH` | `~/.config/robotiko-mcp-gdrive/tokens.json` | Saved auth token |

## Security

- OAuth credentials and tokens are stored in `~/.config/`, NOT in the repo
- `.gitignore` excludes all credential files
- The server only accesses Google Drive — no other Google services
- Scopes limited to `drive.file` and `drive` (read/write Drive files only)
