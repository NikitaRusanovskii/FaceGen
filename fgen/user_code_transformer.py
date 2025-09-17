import ast
from pathlib import Path


class UserCodeTransformer(ast.NodeTransformer):
    def __init__(self, path_to_user_file: Path,
                 imodule_path: Path):
        self.path_to_user_file = path_to_user_file
        self.imodule_path = imodule_path

    def visit_ClassDef(self, node):
        node.decorator_list = [
            d for d in node.decorator_list
            if not (isinstance(d, ast.Name) and d.id == 'face')
        ]

        node.bases.append(ast.Name(f'I{node.name}', ctx=ast.Load()))
        return self.generic_visit(node)

    def visit_FunctionDef(self, node):
        node.decorator_list = [
            d for d in node.decorator_list
            if not (isinstance(d, ast.Name) and d.id == 'face_method')
        ]
        return self.generic_visit(node)