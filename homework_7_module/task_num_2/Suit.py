from homework_7_module.task_num_2.AbstractFabricConsumption import AbstractFabricConsumption


class Suit(AbstractFabricConsumption):
    def __init__(self, h):
        self.h = h

    @property
    def fabric_consumption(self):
        return 2 * self.h + 0.3
