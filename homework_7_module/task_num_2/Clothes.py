from homework_7_module.task_num_2.AbstractFabricConsumption import AbstractFabricConsumption
from homework_7_module.task_num_2.Coat import Coat
from homework_7_module.task_num_2.Suit import Suit


class Clothes(AbstractFabricConsumption):
    def __init__(self, title):
        self.title = title
        self.clothes = []

    def add_coat(self, v):
        self.clothes.append(Coat(v))

    def add_suit(self, h):
        self.clothes.append(Suit(h))

    @property
    def fabric_consumption(self):
        main_fabric_consumption = 0
        for item in self.clothes:
            main_fabric_consumption += item.fabric_consumption
        return "Расход ткани " + self.title + " = " + str(main_fabric_consumption)
