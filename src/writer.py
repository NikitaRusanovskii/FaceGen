from pathlib import Path
from abc import ABC, abstractmethod


"""Этот компонент ответственнен только за работу с файлами"""


FIRTS_LINE_IN_FILE = 'from abc import ABC, abstractmethod\n\n'


class IWriter(ABC):
    @abstractmethod
    def _create_file(self, path_to_file: Path) -> None:
        pass

    @abstractmethod
    def write_in_file(self, data: str) -> None:
        pass


class Write(IWriter):
    def __init__(self):
        self.path_to_file: Path | None = None

    def _create_file(self, path_to_file: Path):
        with open(path_to_file, 'w') as ftw:  # file to write
            ftw.write(FIRTS_LINE_IN_FILE)  # я думаю, от этого можно избавиться
