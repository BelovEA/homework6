import time
class TrafficLight:
    __color = "Red, Yellow, Green"
    def running(self):
        while True:
            print("Red")
            time.sleep(7)
            print("Yellow")
            time.sleep(2)
            print("Green")
            time.sleep(5)
a = TrafficLight()
a.running()

