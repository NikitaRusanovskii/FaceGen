from typing import Callable


"""Компонент ответственнен только за подмену реализаций интерфейсов"""


def face(func: Callable):
    def wrapper(*args, **kwargs):
        return {'face_mock': 'called'}
    return wrapper


def face_method(func: Callable):
    def wrapper(*args, **kwargs):
        return {'face_method_mock': 'called'}
    return wrapper
