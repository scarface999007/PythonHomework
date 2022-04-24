# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(num_a, num_b):
    return num_a / num_b


num = input("Введите два числа: ").split(" ")
numA = int(num[0])
numB = int(num[1])

try:
    res = division(numA, numB)
    print(res)
except ZeroDivisionError:
    print("Деление на 0!")

# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
#    имя, фамилия, год рождения, город проживания, email, телефон.
#    Функция должна принимать параметры как именованные аргументы.
#    Осуществить вывод данных о пользователе одной строкой.

userData = ["Name1", "Surname1", 1991, "City1", "email@email.com", "+79998887755"]


def get_user_info(name, surname, birth_date, city, email, phone_num):
    return " ".join((name, surname, str(birth_date), city, email, phone_num))


print(get_user_info(surname=userData[1], name=userData[0], birth_date=userData[2], city=userData[3], email=userData[4],
                    phone_num=userData[5]))


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
#    возвращает сумму наибольших двух аргументов.

def my_func(num_a, num_b, num_c):
    my_list = [num_a, num_b, num_c]
    max_num_1 = max(my_list)
    my_list.remove(max_num_1)
    max_num_2 = max(my_list)
    return max_num_1 + max_num_2


print("Сумма двух максимальных элементов: " + str(my_func(4, 2, 4)))


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
#    Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
#    При решении задания нужно обойтись без встроенной функции возведения числа в степень.


def my_func(x, y):
    return x ** y


print(my_func(3.1, -2))


# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
#    При нажатии Enter должна выводиться сумма чисел.
#    Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
#    Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
#    Но если вместо числа вводится специальный символ, выполнение программы завершается.
#    Если специальный символ введён после нескольких чисел,
#    то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def my_sum(list_num):
    total = 0
    for item in list_num:
        total += int(item)
    return total


sum_num = 0
while True:
    isExit = False
    inputData = input("Введите числа через пробел (для выхода введите q): ").split(" ")
    if inputData[len(inputData) - 1] == 'q':
        inputData.pop()
        isExit = True
    sum_num += my_sum(inputData)
    print("Сумма чисел: " + str(sum_num))
    if isExit:
        break


# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
#    но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(word):
    return str(word).title()


print(int_func("text"))

# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
#    Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
#    но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

inputData = input("Введите слова через пробел состоящие из латинских букв в нижнем регистре: ").split(" ")
resultList = []
for item in inputData:
    resultList.append(int_func(item))
print(" ".join(resultList))
