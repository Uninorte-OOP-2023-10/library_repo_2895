import os

from static.config import PROJECT_ABSPATH, DATA_DIR

class FileManager:

    DATA_PATH = os.path.join(PROJECT_ABSPATH, DATA_DIR)

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def generate_path(self) -> str:
        return os.path.join(FileManager.DATA_PATH, self.filename)