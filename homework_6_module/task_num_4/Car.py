class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Go")

    def stop(self):
        print("Stop")

    def turn(self, direction):
        print("Turn " + direction)

    def show_speed(self):
        print("Текущая скорость " + str(self.speed))
