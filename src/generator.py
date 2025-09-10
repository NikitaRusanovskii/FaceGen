import ast
from abc import ABC, abstractmethod


"""Этот компонент ответственнен только за создание кода из AST"""


class IDataGenerator(ABC):
    @abstractmethod
    def data_generate(self) -> str:
        pass


class DataGenerator(IDataGenerator):
    def __init__(self, iclass_dict: dict[str, list[str]]):
        self.iclass_dict = iclass_dict

    def _complete_modules(self, *args: list) -> ast.Module:
        module = ast.Module(
            body=list(args),
            type_ignores=[]
        )

        ast.fix_missing_locations(module)
        return module

    def _create_import_from(self) -> ast.ImportFrom:
        # позже добавлю возможность нескольких импортов
        import_from_abc = ast.ImportFrom(
            module='abc',
            names=[
                ast.alias(name='ABC', asname=None),
                ast.alias(name='abstractmethod', asname=None)
            ],
            level=0,  # уровень импорта
        )
        return import_from_abc

    def _create_function(self, name: str):
        fn = ast.FunctionDef(name=name,
                             decorator_list=[ast.Name(id='abstractmethod',
                                             ctx=ast.Load())],
                             body=[ast.Pass()],
                             args=ast.arguments(args=[ast.arg(arg='self')],
                                                posonlyargs=[],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=[],
                                                defaults=[]))
        return fn

    def _create_interface_classes(self):
        classes = []
        for _class, _methods in self.iclass_dict.items():
            methods = []
            for method in _methods:
                _ = self._create_function(method)
                methods.append(_)

            interface_class = ast.ClassDef(
                name=f'I{_class}',
                bases=[ast.Name(id='ABC', ctx=ast.Load())],
                keywords=[],
                decorator_list=[],
                body=methods  # заполнить функциями
            )
            classes.append(interface_class)
        return classes

    def data_generate(self) -> str:
        import_from_abc = self._create_import_from()
        interface_class = self._create_interface_classes()

        return ast.unparse(self._complete_modules(import_from_abc,
                                                  *interface_class))
