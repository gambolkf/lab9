import os


class PathNotExisting(Exception):
    pass


class File:
    def __init__(self, path):
        self._path = self.set_path(path)

    def info(self, path):
        file_name = os.path.basename(path)
        line_count = 0
        with open(path, 'r') as file:
            for line in file:
                line_count += 1
        dir_name = os.path.dirname(path)