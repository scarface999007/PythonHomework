from homework_8_module.task_num_4.OfficeEquipment import OfficeEquipment


class Xerox(OfficeEquipment):
    def __init__(self, type, model, price, print_speed):
        super().__init__(type, model, price)
        self.print_speed = print_speed
