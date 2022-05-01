import json
import re

# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#    Об окончании ввода данных будет свидетельствовать пустая строка.

with open("homework_5_files/homework5_first_file", 'w') as first_file:
    while True:
        line = input("Введите строку текста(для выхода оставьте строку пустой и нажмите Enter): ")
        if not line:
            break
        first_file.write(line + "\n")

# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
#    выполнить подсчёт строк и слов в каждой строке.

with open("homework_5_files/homework5_second_file", 'r') as second_file:
    line_count = 0
    word_count = 0
    for i, line in enumerate(second_file):
        line_count += 1
        for el in line.split(" "):
            word_count += 1
        print("Количество слов в строке " + str(i + 1) + ": " + str(word_count))
        word_count = 0
    print("Количество строк: " + str(line_count))


# 3. Создать текстовый файл (не программно).
#    Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
#    Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
#    Выполнить подсчёт средней величины дохода сотрудников.

with open("homework_5_files/homework5_third_file", 'r') as third_file:
    employees = []
    income = 0
    employees_count = 0
    for line in third_file:
        employees_count += 1
        data = line.split(" ")
        salary = float(data[1])
        income += salary
        if salary < 20000:
            employees.append(data[0])
    print("Сотрудники с окладом менее 20 тысяч: " + str(employees))
    print("Средняя величина дохода сотрудников: " + str(income / employees_count))

# 4. Создать (не программно) текстовый файл со следующим содержимым:
#    One — 1
#    Two — 2
#    Three — 3
#    Four — 4
#    Напишите программу, открывающую файл на чтение и считывающую построчно данные.
#    При этом английские числительные должны заменяться на русские.
#    Новый блок строк должен записываться в новый текстовый файл.

numerals = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", }
with open("homework_5_files/homework5_fourth_file", 'r') as fourth_file, open(
        "homework_5_files/new_homework5_fourth_file", 'w') as new_fourth_file:
    for line in fourth_file:
        data = line.split(" - ")
        new_num = numerals[data[0]]
        data.remove(data[0])
        data.insert(0, new_num)
        new_data = data[0] + " - " + data[1]
        new_fourth_file.write(new_data)

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
#    Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open("homework_5_files/homework5_fifth_file", 'w') as fifth_file:
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fifth_file.write(" ".join(map(str, num_list)))

with open("homework_5_files/homework5_fifth_file", 'r') as fifth_file:
    sum_num = 0
    new_num_list = fifth_file.read().split(" ")
    for num in new_num_list:
        sum_num += int(num)
    print(sum_num)

# 6. Сформировать (не программно) текстовый файл.
#    В нём каждая строка должна описывать учебный предмет и наличие лекционных,
#    практических и лабораторных занятий по предмету.
#    Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
#    Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

subj = {}
with open("homework_5_files/homework5_sixth_file", 'r', encoding='utf_8') as sixth_file:
    for line in sixth_file:
        data = line.split(":")
        subject = data[0]
        s = [int(num) for num in re.findall(r'-?\d+', data[1])]
        subj[subject] = sum(s)
    print(subj)


# 7. Создать вручную и заполнить несколькими строками текстовый файл,
#    в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
#    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#    Если фирма получила убытки, в расчёт средней прибыли её не включать.
#    Далее реализовать список.
#    Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#    Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#    Итоговый список сохранить в виде json-объекта в соответствующий файл.

with open("homework_5_files/homework5_seventh_file", 'r') as seventh_file:
    firm_list = []
    average_profit = 0
    for line in seventh_file:
        dictionary = {}
        firm, type_of_ownership, profit, expenses = line.split(" ")
        if profit > expenses:
            average_profit += int(profit)
        dictionary[firm] = abs(int(profit) - int(expenses))
        firm_list.append(dictionary)
    firm_list.append({"average_profit": average_profit})
    print(firm_list)


with open("homework_5_files/homework5_seventh_file_json", 'w') as seventh_file:
    json.dump(firm_list, seventh_file)

