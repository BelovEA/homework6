import time
class TrafficLight:
    __color = "Red, Green, Yellow"
    def running(self):
        while True:
            print("Red")
            time.sleep(7)
            print("Green")
            time.sleep(2)
            print("Yellow")
            time.sleep(5)
a = TrafficLight()
print(a.running())

