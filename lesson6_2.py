#2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def calc(self, weight =26, thickness = 5):
        return f"{self._length * self._width * weight * thickness / 1000}"

road = Road(2000, 14)
print(road.calc())