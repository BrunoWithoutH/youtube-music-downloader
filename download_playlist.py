#!/usr/bin/env python3
"""
YouTube Playlist to MP3 Downloader
Downloads all videos from a YouTube playlist as MP3 files with metadata.
"""

import sys
import os
import yt_dlp


def download_playlist_as_mp3(playlist_url, output_dir='downloads'):
    """
    Download all videos from a YouTube playlist as MP3 files with metadata.
    
    Args:
        playlist_url (str): The URL of the YouTube playlist
        output_dir (str): Directory where MP3 files will be saved (default: 'downloads')
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }, {
            'key': 'FFmpegMetadata',
            'add_metadata': True,
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
        'extract_flat': False,
        'writethumbnail': False,
        'embedthumbnail': False,
        'addmetadata': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Fetching playlist information from: {playlist_url}")
            
            # Extract playlist info
            playlist_info = ydl.extract_info(playlist_url, download=False)
            
            if 'entries' not in playlist_info:
                print("Error: This doesn't appear to be a valid playlist URL")
                return
            
            total_videos = len([e for e in playlist_info['entries'] if e])
            print(f"\nFound {total_videos} videos in the playlist")
            print(f"Downloads will be saved to: {os.path.abspath(output_dir)}\n")
            
            # Download the playlist
            ydl.download([playlist_url])
            
            print(f"\n✓ Successfully downloaded {total_videos} songs!")
            
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        sys.exit(1)


def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) < 2:
        print("YouTube Playlist to MP3 Downloader")
        print("\nUsage:")
        print(f"  python {os.path.basename(__file__)} <playlist_url> [output_directory]")
        print("\nExample:")
        print(f"  python {os.path.basename(__file__)} https://www.youtube.com/playlist?list=PLxx... downloads")
        print("\nDefault output directory is 'downloads' if not specified.")
        sys.exit(1)
    
    playlist_url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else 'downloads'
    
    download_playlist_as_mp3(playlist_url, output_dir)


if __name__ == '__main__':
    main()
