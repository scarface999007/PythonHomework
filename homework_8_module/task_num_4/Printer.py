from homework_8_module.task_num_4.OfficeEquipment import OfficeEquipment


class Printer(OfficeEquipment):
    def __init__(self, type, model, price, is_color_printer):
        super().__init__(type, model, price)
        self.is_color_printer = is_color_printer
