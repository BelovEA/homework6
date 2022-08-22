class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
class TypeA(Road):
    def __init__(self, length, width):
        self._length = length
        self._width = width
        mass = 25,7
        calc = length * width * mass * 5
        return calc
class TypeB(Road):
    def __init__(self, length, width):
        self._length = length
        self._width = width
        mass = 24,6
        calc = length * width * mass * 5
        return calc
class TypeC(Road):
    def __init__(self, length, width):
        self._length = length
        self._width = width
        mass = 24,9
        calc = length * width * mass * 5
        return calc
a1 = TypeA(int(input()), int(input()))
print(TypeA)