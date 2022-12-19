#5
class Stationery:
    def __init__(self, title="возьмите в руку карандаш, ручку или маркер"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")

class Pen(Stationery):

    def draw(self):
        print(f"Начинаем выписывать при помощи {self.title}")

class Pencil(Stationery):

    def draw(self):
        print(f"Начинаем чертить  при помощи {self.title}")

class Handle(Stationery):

    def draw(self):
        print(f"Начинаем отмечать при помощи {self.title}")

example = Stationery()
pen = Pen("Ручки")
pencil = Pencil("Карандаша")
handle = Handle("Маркера")

stat = [pen, pencil, handle]

for i in stat:
    i.draw()