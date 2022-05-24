from homework_8_module.task_num_4.OfficeEquipment import OfficeEquipment


class Scanner(OfficeEquipment):
    def __init__(self, type, model, price, resolution):
        super().__init__(type, model, price)
        self.resolution = resolution