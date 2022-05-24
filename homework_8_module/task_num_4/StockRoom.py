from homework_8_module.task_num_4.OfficeEquipment import OfficeEquipment
from homework_8_module.task_num_4.OfficeEquipmentType import OfficeEquipmentType


class StockRoom:
    def __init__(self, title, area):
        self.title = title
        self.area = area
        self.office_equipment_list = []

    def add_office_equipment(self, office_equipment):
        try:
            if not isinstance(office_equipment, OfficeEquipment):
                raise TypeError("Error: Добавление объекта с некорректным типом данных")
            self.office_equipment_list.append(office_equipment)
        except TypeError as err:
            print(err)

    def remove_office_equipment(self, office_equipment):
        try:
            if not isinstance(office_equipment, OfficeEquipment):
                raise TypeError("Error: Удаление объекта с некорректным типом данных")
            self.office_equipment_list.remove(office_equipment)
        except TypeError as err:
            print(err)

    def office_equipment_info(self):
        my_dict = {}
        printer_count = 0
        scanner_count = 0
        xerox_count = 0
        for office_equipment in self.office_equipment_list:
            if office_equipment.type == OfficeEquipmentType.PRINTER:
                printer_count += 1
            if office_equipment.type == OfficeEquipmentType.SCANNER:
                scanner_count += 1
            if office_equipment.type == OfficeEquipmentType.XEROX:
                xerox_count += 1

        if printer_count != 0:
            my_dict[OfficeEquipmentType.PRINTER.value] = printer_count

        if scanner_count != 0:
            my_dict[OfficeEquipmentType.SCANNER.value] = scanner_count

        if xerox_count != 0:
            my_dict[OfficeEquipmentType.XEROX.value] = xerox_count

        return my_dict
