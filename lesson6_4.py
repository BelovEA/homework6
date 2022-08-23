class Car:
    def __init__(self, n, c, s, p = False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = True
    def go(self):
        print(f"{self.name} - on start!")

    def stop(self):
        print(f"{self.name} stop!")

    def turn(self):
        pass

    def show_speed(self):
        return f"{self.name} speed - {self.speed}"

class TownCar(Car):

    def show_speed(self):
        return f"{self.name} speed - {self.speed} is OVER SPEED, STOP!" if self.speed > 60 else super().show_speed()

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        return f"{self.name} speed - {self.speed} is OVER SPEED, STOP!" if self.speed > 40 else super().show_speed()

class PoliceCar(Car):
    def __init__(self, n, c, s):
        super().__init__(n, c, s, p=True)
towncar = TownCar("Nissan", "white", 60)
sport_car = SportCar("Bollid", "yellow", 180)
work_car = WorkCar("Toyta", "blue", 65)
police_car = PoliceCar("Lada", "black", 80)

cars = [towncar, sport_car, work_car, police_car]

for i in cars:
    i.go()
    print(i.show_speed())