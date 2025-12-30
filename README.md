# YouTube Music Downloader

A Python script that downloads all videos from a YouTube playlist as MP3 files with metadata (Artist, Title, etc.).

## Features

- Download entire YouTube playlists as MP3 files
- Automatically extracts and embeds metadata (Artist, Title)
- High quality audio (192 kbps)
- Simple command-line interface

## Requirements

- Python 3.6 or higher
- FFmpeg (required by yt-dlp for audio conversion)

### Installing FFmpeg

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

## Installation

1. Clone this repository:
```bash
git clone https://github.com/BrunoWithoutH/youtube-music-downloader.git
cd youtube-music-downloader
```

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python download_playlist.py <playlist_url>
```

Specify output directory:
```bash
python download_playlist.py <playlist_url> <output_directory>
```

### Examples

Download playlist to default 'downloads' folder:
```bash
python download_playlist.py "https://www.youtube.com/playlist?list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf"
```

Download playlist to custom folder:
```bash
python download_playlist.py "https://www.youtube.com/playlist?list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf" my_music
```

## Output

- MP3 files are saved with the video title as filename
- Metadata (Artist, Title) is automatically extracted from YouTube and embedded in the MP3 files
- Default output directory is `downloads/` (created automatically if it doesn't exist)

## License

See LICENSE file for details.