from mp3_tagger import MP3File


def tag(file, artist="", track="", album=""):
    mp3 = MP3File(file)
    if artist:
        mp3.artist = artist
    if track:
        mp3.track = track
    if album:
        mp3.album = album
    mp3.save()
