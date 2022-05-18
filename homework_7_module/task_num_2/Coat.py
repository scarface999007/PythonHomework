from homework_7_module.task_num_2.AbstractFabricConsumption import AbstractFabricConsumption


class Coat(AbstractFabricConsumption):
    def __init__(self, v):
        self.v = v

    @property
    def fabric_consumption(self):
        return self.v / 6.5 + 0.5
