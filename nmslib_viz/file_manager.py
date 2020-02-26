import os


def exists(file_path: str):
    return os.path.isfile(file_path)
