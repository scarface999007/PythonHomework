from homework_6_module.task_num_4.Car import Car


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")
        else:
            print("Текущая скорость " + str(self.speed))
