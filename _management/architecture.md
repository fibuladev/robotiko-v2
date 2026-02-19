# SYSTEM ARCHITECTURE

## 1. TECHNICAL STACK
* **Version Control:** GitHub (Brain)
* **Storage:** AWS S3 (Long-term Archive for heavy video assets)
* **Automation:** GitHub Actions + Python Scripts
* **Local Workspace:** Where the actual rendering happens (GPU dependent)

## 2. DATA FLOW
`Lyrics (Text)` -> `Suno (Audio)` -> `LLM (Script)` -> `Nano Banana (Img)` -> `Kling (Video)` -> `CapCut (Final)`

## 3. FOLDER MIRRORING
The structure on Local Machine is mirrored to S3 for backup.
`Local/episode-01/raw` == `S3/robotiko-bucket/episode-01/raw`