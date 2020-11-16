def get_info(file):
    with open(file, "r") as f:
        header = next(f)
        album_name, artist = header.split(",")
        return album_name, artist


def read_playlist(file):
    with open(file, "r") as f:
        next(f)
        for i, line in enumerate(f):
            yield (str(i + 1), *line.rstrip("\n").split(","))
