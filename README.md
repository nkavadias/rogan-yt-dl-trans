# rogan-yt-dl-trans

Automated transcript downloader for Joe Rogan Experience YouTube playlist using yt-dlp.

## Features

- 📥 Download transcripts from YouTube playlists without downloading videos
- 🤖 Automated execution via GitHub Actions (on-demand or scheduled)
- 🔄 Skip already downloaded transcripts (no overwrites)
- 📝 Download auto-generated subtitles in TTML format
- 🎯 English language subtitles

## Usage

### Option 1: Run via GitHub Actions (Recommended)

1. Go to the **Actions** tab in this repository
2. Select **Download Transcripts** workflow
3. Click **Run workflow** button
4. Wait for the workflow to complete
5. Download the transcripts artifact from the workflow run

The workflow can also be scheduled to run automatically (currently set to weekly).

### Option 2: Run Locally

#### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

#### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/nkavadias/rogan-yt-dl-trans.git
   cd rogan-yt-dl-trans
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### Running the Script

Simply run the Python script:

```bash
python download_transcripts.py
```

Transcripts will be downloaded to the `transcripts/` directory.

### Option 3: Manual yt-dlp Command

If you prefer to run yt-dlp directly:

1. Install yt-dlp:
   ```bash
   pip install yt-dlp
   ```

2. Run the command:
   ```bash
   yt-dlp "https://www.youtube.com/playlist?list=UUzQUP1qoWDoEbmsQxvdjxgQ" \
     --write-sub \
     --sub-langs=en \
     --write-auto-subs \
     --sub-format "ttml" \
     --skip-download \
     --no-overwrites \
     -o 'transcripts/%(title)s[%(id)s].%(ext)s'
   ```

## Configuration

### Customizing the Script

Edit `download_transcripts.py` to customize:
- **Playlist URL**: Change the `playlist_url` variable
- **Output directory**: Change the `output_dir` variable
- **Subtitle format**: Modify the `--sub-format` parameter (options: ttml, vtt, srv3, srv2, srv1, json3)
- **Language**: Change `--sub-langs` parameter (e.g., `en`, `es`, `fr`)

### Customizing the Workflow

Edit `.github/workflows/download-transcripts.yml` to:
- Change the schedule (modify the `cron` expression)
- Adjust artifact retention days
- Add notification steps

## Output

Transcripts are saved with the following naming convention:
```
transcripts/[Video Title][Video ID].en.ttml
```

Example:
```
transcripts/Joe Rogan Experience #1234 - Guest Name[abc123xyz].en.ttml
```

## License

See [LICENSE](LICENSE) file for details.

## Notes

- The `transcripts/` directory is ignored by git (see `.gitignore`)
- Existing transcripts are not overwritten (controlled by `--no-overwrites` flag)
- Only English auto-generated subtitles are downloaded by default