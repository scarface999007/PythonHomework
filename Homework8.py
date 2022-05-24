from homework_8_module.ComplexNumber import ComplexNumber
from homework_8_module.Date import Date
from homework_8_module.InputNumError import InputNumError
from homework_8_module.ZeroDivError import ZeroDivError
from homework_8_module.task_num_4.OfficeEquipmentType import OfficeEquipmentType
from homework_8_module.task_num_4.Printer import Printer
from homework_8_module.task_num_4.Scanner import Scanner
from homework_8_module.task_num_4.StockRoom import StockRoom
from homework_8_module.task_num_4.Xerox import Xerox

# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
#    строки формата «день-месяц-год».

date_str = "19-05-2022"
date = Date(date_str)
Date.date_to_int(date_str)
Date.date_to_int(date_str + "1")

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.

try:
    input_num = int(input("Введите число: "))
    if input_num == 0:
        raise ZeroDivError("На ноль делить нельзя")
    res = 100 / input_num
except ZeroDivError as err:
    print(err)
else:
    print("Результат = " + str(res))

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.

my_list = []
while True:
    try:
        data = input("Введите число(для выхода введите 'q'): ")
        if data == 'q':
            break
        if not data.isdigit():
            raise InputNumError("Значение: " + data + " не является числом")
        my_list.append(int(data))
    except InputNumError as err:
        print(err)
print(my_list)

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
#    А также класс «Оргтехника», который будет базовым для классов-наследников.

stock_room = StockRoom("StockRoom1", 1000)
printer1 = Printer(OfficeEquipmentType.PRINTER, "Printer model 1", 1000, True)
scanner1 = Scanner(OfficeEquipmentType.SCANNER, "Scanner model 1", 1000, 1920)
xerox1 = Xerox(OfficeEquipmentType.XEROX, "Xerox model 1", 1000, 10)

printer2 = Printer(OfficeEquipmentType.PRINTER, "Printer model 2", 2000, False)
scanner2 = Scanner(OfficeEquipmentType.SCANNER, "Scanner model 2", 2000, 640)
xerox2 = Xerox(OfficeEquipmentType.XEROX, "Xerox model 2", 2000, 20)

# 5. Разработайте методы, которые отвечают за приём оргтехники на склад и
#    передачу в определённое подразделение компании.

stock_room.add_office_equipment(printer1)
stock_room.add_office_equipment(scanner1)
stock_room.add_office_equipment(xerox1)
stock_room.add_office_equipment(printer2)
stock_room.add_office_equipment(scanner2)
stock_room.add_office_equipment(xerox2)
print(stock_room.office_equipment_info())

stock_room.remove_office_equipment(printer1)
stock_room.remove_office_equipment(xerox2)
print(stock_room.office_equipment_info())

# 6. Реализуйте механизм валидации вводимых пользователем данных.

stock_room.add_office_equipment(1)
stock_room.remove_office_equipment(1)

# 7. Реализовать проект «Операции с комплексными числами».

complex_num1 = ComplexNumber(1, 2)
complex_num2 = ComplexNumber(3, 4)
print(complex_num1 + complex_num2)
print(complex_num1 * complex_num2)
