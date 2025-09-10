# 📖 FaceGen

**FaceGen** — это библиотека для автоматической генерации интерфейсов в Python на основе исходного кода.
Идея вдохновлена принципами **чистой архитектуры (Clean Architecture)**, а также идеями из книги Роберта Мартина:

* **Analyzer** — ищет классы и методы, помеченные специальными декораторами.
* **Generator** — создает интерфейсы (абстрактные классы).
* **Writer** — отвечает за сохранение интерфейсов в файлы.
* **Mocker** — подменяет реализации интерфейсов для тестов.

---

## ✨ Возможности

* Поиск классов с декоратором `@face`.
* Поиск методов класса с декоратором `@face_method`.
* Генерация интерфейсов с абстрактными методами.
* Автоматическая запись интерфейсов в `.py` файлы.
* Простая система моков для подмены зависимостей.

---

## 🚀 Установка

```bash
git clone https://github.com/yourname/facegen.git
cd facegen
```

(позже можно добавить `pip install facegen`, если сделаешь пакет)

---

## 🛠 Использование

### 1. Помечаем классы и методы

```python
from facegen.mocker import face, face_method


@face
class Calc:
    def __init__(self, mode: str):
        self.mode = mode

    @face_method
    def calculate(self):
        if self.mode == "standart":
            print("it's standart mode")
```

### 2. Запускаем анализ и генерацию

```python
from facegen.analyzer import ASTAnalyzer, TreeVisitor
from facegen.generator import DataGenerator
from pathlib import Path

tv = TreeVisitor()
analyzer = ASTAnalyzer(tv)

iclass_dict = analyzer.analyze(Path("src/test.py"))

generator = DataGenerator(iclass_dict=iclass_dict)
code = generator.data_generate()
print(code)
```

### 3. Результат (генерируемый интерфейс)

```python
from abc import ABC, abstractmethod

class ICalc(ABC):
    @abstractmethod
    def calculate(self):
        pass
```

---

## 📂 Структура проекта

```
src/
 ├── analyzer.py   # анализ исходного кода (AST)
 ├── generator.py  # генерация интерфейсов
 ├── writer.py     # работа с файлами
 ├── mocker.py     # декораторы и моки
 ├── test.py       # пример исходного кода
 └── main.py       # пример пайплайна
tests/
 ├── test_analyzer.py
 ├── test_generator.py
 ├── test_writer.py
 └── test_mocker.py
```

---

## ✅ Планы

* [ ] CLI (`facegen -f src/test.py -o interfaces/`)
* [ ] Расширенные моки (`FaceMock`, `FaceMockGroup`)
* [ ] Поддержка декораторов с аргументами
* [ ] CI и тесты

---

## 📜 Лицензия

MIT.
