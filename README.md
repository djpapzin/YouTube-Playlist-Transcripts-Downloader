# YouTube Playlist Transcripts Downloader

This script allows you to download transcripts (subtitles) of all videos in a given YouTube playlist. Transcripts are saved as `.srt` files, which are named after the video titles and stored in a folder named after the playlist.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-github-username/your-repository-name.git
   cd your-repository-name
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python script.py
   ```

2. The script will fetch the playlist and display the total number of videos. It will then start downloading the transcripts for each video, showing progress and the number of videos remaining.

3. Once completed, you'll find the transcripts in the `transcripts` directory, inside a folder named after the playlist.

## Dependencies

- `pytube`: For fetching YouTube video and playlist details.
- `youtube_transcript_api`: For downloading the transcripts.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)