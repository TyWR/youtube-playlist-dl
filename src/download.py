import subprocess
import hashlib


def generate_sha1(string):
    m = hashlib.sha1()
    m.update(string.encode())
    return m.hexdigest()


def download_mp3(url: str, name: str = ""):
    name = generate_sha1(url) if not len(name) else name
    cmd = [
        "youtube-dl",
        "--extract-audio",
        "--audio-quality",
        "0",
        "--audio-format",
        "mp3",
        "-o",
        f"{name}.%(ext)s",
        url,
    ]
    subprocess.Popen(cmd).wait()
    return f"{name}.mp3"
