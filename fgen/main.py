import argparse
from .analyzer import ASTAnalyzer, TreeVisitor
from .generator import DataGenerator, write_in_file
from pathlib import Path


class App:
    def __init__(self,
                 path_to_file: Path,
                 path_to_interface_file: Path):
        self.path_to_file = path_to_file
        self.path_to_interface_file = path_to_interface_file
        self.tv = TreeVisitor()
        self.analyzer = ASTAnalyzer(self.tv)

    def run(self):
        iclass_dict = self.analyzer.analyze(path_to_file=self.path_to_file)
        my_generator = DataGenerator(iclass_dict=iclass_dict)

        scanned_code = my_generator.data_generate()

        write_in_file(self.path_to_interface_file, scanned_code)


parser = argparse.ArgumentParser(
    prog="fgen",
    description="A utility for automatically generating\
                 interfaces based on ready-made implementations."
)

parser.add_argument("path_file",
                    help="Path to the file with the implementation")
parser.add_argument("path_interface",
                    help="Path to the generated file with interfaces")


def main():
    args = parser.parse_args()
    path_to_file = Path(args.path_file)
    path_to_interface = Path(args.path_interface)
    app = App(path_to_file=path_to_file,
              path_to_interface_file=path_to_interface)

    app.run()
