from .analyzer import ASTAnalyzer, TreeVisitor
from .generator import DataGenerator
from pathlib import Path


path_to_file = Path('src/test.py')
tv = TreeVisitor()
analyzer = ASTAnalyzer(tv)

iclass_dict = analyzer.analyze(path_to_file=path_to_file)


my_generator = DataGenerator(iclass_dict=iclass_dict)
scode = my_generator.data_generate()
print(scode)
