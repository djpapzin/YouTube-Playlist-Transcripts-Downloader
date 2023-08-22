import os
import youtube_dl
from tqdm import tqdm

def download_transcripts(playlist_url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'subtitlesformat': 'vtt',
        'outtmpl': 'transcripts/%(playlist)s/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegSubtitlesConvertor',
            'format': 'srt',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=False)
        playlist_title = info_dict.get('title', None)

        # Create a directory named after the playlist
        if not os.path.exists(f'transcripts/{playlist_title}'):
            os.makedirs(f'transcripts/{playlist_title}')

        # Downloading transcripts
        print(f"\033[94mDownloading transcripts for playlist: {playlist_title}\033[0m")
        entries = info_dict.get('entries', [])
        total_videos = len(entries)
        print(f"\033[93mTotal videos in the playlist: {total_videos}\033[0m")

        for idx, entry in enumerate(tqdm(entries, desc="Downloading", ncols=100)):
            ydl.download([entry['url']])
            print(f"\033[95mVideos remaining: {total_videos - idx - 1}\033[0m")

if __name__ == '__main__':
    playlist_url = "https://www.youtube.com/watch?v=2lkXYYEBqdo&list=PLZR2LyEirbnu-3QMRN99tdLXHI1GJotBl&ab_channel=KingKongConsciousness"
    download_transcripts(playlist_url)