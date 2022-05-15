from homework_6_module.task_num_5.Stationery import Stationery


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки " + self.title)
