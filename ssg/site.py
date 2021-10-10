from os import mkdir
from pathlib import Path


class Site:

    def __init__(self, source, dest) -> None:
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest/path.relative_to(self.source)
        #debugging statement
        print(directory)

        directory.mkdir(parents=True, exists_ok=True)
        print(directory)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
