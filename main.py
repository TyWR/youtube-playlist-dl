import argparse
import os

from src.download import download_mp3
from src.read_playlist import read_playlist, get_info
from src.tag import tag

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Download playlist as album.")
    parser.add_argument(
        "playlist",
        metavar="playlist",
        type=str,
        help="a file containing the info of all the tracks.",
    )

    args = parser.parse_args()
    base_path = os.path.splitext(args.playlist)[0]
    os.makedirs(base_path, exist_ok=True)

    album, artist = get_info(args.playlist)
    for track, name, url in read_playlist(args.playlist):
        track_file = download_mp3(url, name=os.path.join(base_path, name))
        tag(track_file, artist=artist, track=track, album=album)
