# Robotiko Google Drive MCP Server

Custom MCP server for managing binary assets (PNG, MP4, WAV) on Google Drive.
Built for the Robotiko v2.0 production pipeline.

## Why Custom?

We don't use third-party MCP packages. This server is ~600 lines of code (`src/auth.js` +
`src/index.js` + `src/tools.js`) with only two dependencies:
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
2. Sign in with the Google account that owns the target Drive folder
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

This tries to open your default browser (Windows, macOS, and Linux are all handled). If it
cannot, it prints the authorization URL — open that manually. Sign in with the Google account
that owns the target Drive folder and grant permissions.
Token is saved to `~/.config/robotiko-mcp-gdrive/tokens.json`.

### Step 5: Verify the Claude Code registration

The repo already ships a `.mcp.json` in the **project root** (not inside `.claude/`). Open it,
confirm it matches the block below, and adjust the paths only if your layout differs:

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
> A config placed inside `.claude/` is not read — tools will silently fail to load.

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

## Usage Walkthrough: Uploading Episode Assets

This walkthrough shows a real production session — uploading EP04's 54 selected images to Google Drive via Claude Code + MCP. Follow along to verify your own setup works.

### 1. Trigger

In Claude Code, use natural language. There is no special command — just describe what you need:

```
"Upload EP04 selected images to Google Drive"
```

Claude reads the `.mcp.json` config at project root, connects to the MCP server, and begins.

### 2. What Happens on Screen

**First, Claude searches for the target folder:**

```
→ mcp__google-drive__gdrive_search({ query: "robotiko" })

← {
    "results": [{
      "id": "1-YXV...",
      "name": "robotiko-v2",
      "type": "folder"
    }],
    "count": 1
  }
```

**Then lists the project structure:**

```
→ mcp__google-drive__gdrive_list_folder({ folderId: "1-YXV..." })

← ep01/ ep02/ ep03/ ep04/
```

**Navigates into the episode folder:**

```
→ mcp__google-drive__gdrive_list_folder({ folderId: "1xW8f..." })

← audio/ raw/ selected/ video/
```

**Uploads files in parallel batches (6 at a time):**

```
→ mcp__google-drive__gdrive_upload({
    localPath: "/path/to/episode-04/04_visuals/selected/ep04_s01_selected.png",
    folderId: "1mbnO..."
  })

← {
    "id": "1ab40...",
    "name": "ep04_s01_selected.png",
    "size": "9.28 MB",
    "link": "https://drive.google.com/file/d/1ab40.../view"
  }
```

Each successful upload returns: file ID, name, size, and a direct Google Drive link.

### 3. Progress

Claude uploads in batches of ~6 files. You will see a counter after each batch:

```
6/54 done. Continuing.
12/54 done. Continuing.
18/54 done. Continuing.
...
54/54 complete!
```

If a file fails (e.g., network timeout), Claude retries it in the next batch automatically. In our EP04 session, `ep04_s30a_selected.png` failed on the first attempt and succeeded on retry.

### 4. Verification

After all uploads, Claude lists the target folder to confirm:

```
→ mcp__google-drive__gdrive_list_folder({ folderId: "1mbnO...", pageSize: 100 })

← 54 files listed, all with correct names and sizes
```

### 5. What You Should See in Google Drive

Open [drive.google.com](https://drive.google.com) and navigate to:

```
robotiko-v2/ep04/selected/
```

You should see all files with the naming convention:
- `ep04_s01_selected.png` through `ep04_s44b_selected.png` (scene images)
- `ep04_ref-char-01.png`, `ep04_ref-env-01.png`, etc. (reference images)
- No S36 or S39 (these share S35's image — by design)

### 6. Token Expiry

OAuth tokens expire after ~1 hour. If you see this error:

```
Error: request to https://oauth2.googleapis.com/token failed
```

The token needs a refresh. Run auth again:

```bash
cd _tools/mcp-gdrive && npm run auth
```

Browser opens, you re-authorize, and uploads resume. This happened during our EP04 session — the fix takes 30 seconds.

### 7. Timing Reference

For EP04 (54 PNG files, ~435 MB total):
- **Upload time:** ~18 minutes (batches of 6, residential internet)
- **Average per file:** ~20 seconds
- **Retries:** 1 (network timeout on S30a, auto-recovered)

---

## Security

- OAuth credentials and tokens are stored in `~/.config/`, NOT in the repo
- `.gitignore` excludes all credential files
- The server only accesses Google Drive — no other Google services
- Scope limited to `drive.file` only (access to files created/opened by this app; not the full Drive)
