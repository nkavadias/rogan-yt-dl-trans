#!/usr/bin/env python3
"""
Script to download transcripts from Joe Rogan Experience YouTube playlist.
Uses yt-dlp to download subtitles/transcripts without downloading videos.
"""

import subprocess
import sys
import os
from pathlib import Path


def main():
    # Configuration
    playlist_url = "https://www.youtube.com/playlist?list=UUzQUP1qoWDoEbmsQxvdjxgQ"
    output_dir = Path("transcripts")
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    # Output template
    output_template = str(output_dir / "%(title)s[%(id)s].%(ext)s")
    
    # yt-dlp command
    cmd = [
        "yt-dlp",
        playlist_url,
        "--write-sub",
        "--sub-langs=en",
        "--write-auto-subs",
        "--sub-format", "ttml",
        "--skip-download",
        "--no-overwrites",
        "-o", output_template
    ]
    
    print(f"Downloading transcripts to: {output_dir}")
    print(f"Command: {' '.join(cmd)}")
    print("-" * 80)
    
    try:
        # Run the command
        result = subprocess.run(cmd, check=True, text=True)
        print("-" * 80)
        print("✓ Transcripts downloaded successfully!")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"✗ Error downloading transcripts: {e}", file=sys.stderr)
        return 1
    except FileNotFoundError:
        print("✗ Error: yt-dlp not found. Please install it first:", file=sys.stderr)
        print("  pip install yt-dlp", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
