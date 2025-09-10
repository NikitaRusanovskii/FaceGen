from mocker import face, face_method


@face
class Calc:
    def __init__(self, mode: str):
        self.mode = mode

    @face_method
    def calculate(self):
        if self.mode == "standart":
            print("it's standart mode")


@face
class Microwave:
    def __init__(self, mode: str):
        self.mode = mode

    @face_method
    def turn_on(self):
        pass

    @face_method
    def turn_off(self):
        pass
