import ast
from pathlib import Path


class TreeVisitor(ast.NodeVisitor):
    def __init__(self):
        super().__init__()
        self.iclass_dict: dict[str, list[str]] | None = None

    def set_iclass_dict(self, iclass_dict: dict[str, list[str]]):
        self.iclass_dict = iclass_dict

    def visit_ClassDef(self, node):
        for dec in node.decorator_list:
            if dec.id == 'face':
                self.iclass_dict[node.name] = []
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                for dec in item.decorator_list:
                    if dec.id == 'face_method':
                        self.iclass_dict[node.name].append(item.name)
        self.generic_visit(node)

    def get_iclass_dict(self):
        return self.iclass_dict


class ASTAnalyzer():
    """Строит и анализирует абстрактное синтаксическое дерево.
    Ищет классы с декоратором @face, а также их методы с декоратором
    @face_method"""
    def __init__(self, tree_visitor: TreeVisitor):
        self.tree_visitor = tree_visitor
        self.iclass_dict: dict[str: list[str]] = {}
        self.tree_visitor.set_iclass_dict(self.iclass_dict)

    def get_ast(self, code: str) -> ast.Module:
        """Возвращает ast строки кода"""
        return ast.parse(code)

    def analyze(self, path_to_file: Path) -> dict[str, list[str]]:
        """Ищет в файле по пути path_to_file все классы с @face
        и их методы с @face_method, а затем возвращает
        словарь [имя класса : методы]"""

        with open(path_to_file.absolute(), 'r') as file:
            sfile = file.read()
            tree = self.get_ast(sfile)
            self.tree_visitor.visit(tree)

        # print(self.iclass_dict)
        return self.iclass_dict
