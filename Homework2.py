# 1. Создать список и заполнить его элементами различных типов данных.
#    Реализовать скрипт проверки типа данных каждого элемента.
#    Использовать функцию type() для проверки типа.
#    Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

myItemList = [1, "2", 3.0, True, [1, 2, 3], (4, 5, 6), {'key1': 'val1', 'key2': 'val2'}, {7, 8, 9}]
for i, item in enumerate(myItemList):
    print("Элемент " + str(i + 1) + " = " + str(myItemList[i]) + ". Тип данных: " + str(type(item)))

# 2. Для списка реализовать обмен значений соседних элементов.
#    Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
#    При нечётном количестве элементов последний сохранить на своём месте.
#    Для заполнения списка элементов нужно использовать функцию input().

items = input("Введите несколько элементов списка через пробел: ").split(" ")
right = len(items) if len(items) % 2 == 0 else len(items) - 1
for i in range(0, right, 2):
    tmp = items[i]
    items[i] = items[i+1]
    items[i+1] = tmp
print(items)


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
#    Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

monthNum = input("Введите номер месяца(1-12): ")
monthList = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
monthDict = {'1': 'Зима', '2': 'Зима', '3': 'Весна',
             '4': 'Весна', '5': 'Весна', '6': 'Лето',
             '7': 'Лето', '8': 'Лето', '9': 'Осень',
             '10': 'Осень', '11': 'Осень', '12': 'Зима', }
print("Список: " + monthList[int(monthNum) - 1])
print("Словарь: " + monthDict[monthNum])

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
#    Вывести каждое слово с новой строки. Строки нужно пронумеровать.
#    Если слово длинное, выводить только первые 10 букв в слове.

words = input("Введите несколько слов через пробел: ").split(" ")
for i, word in enumerate(words):
    print(str(i + 1) + ". " + word[:10])

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
#    У пользователя нужно запрашивать новый элемент рейтинга.
#    Если в рейтинге существуют элементы с одинаковыми значениями,
#    то новый элемент с тем же значением должен разместиться после них.

myList = [8, 7, 6, 5, 5, 3]
num = int(input("Введите число: "))

if num > max(myList):
    myList.insert(0, num)
elif num < min(myList):
    myList.append(num)
elif num in myList:
    index = myList.index(num)
    myList.insert(index, num)
else:
    for i in range(len(myList) - 1):
        if myList[i] > num > myList[i + 1]:
            myList.insert(i+1, num)
            break
print(myList)

# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
#    Каждый кортеж хранит информацию об отдельном товаре.
#    В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
#    название, цена, количество, единица измерения.
#    Структуру нужно сформировать программно, запросив все данные у пользователя.

productList = []
productInputData = None
count = 0
nameProductKey = "название"
priceProductKey = "цена"
countProductKey = "количество"
while True:
    productInputData = input("Введите через пробел название, цену и количество товара (для выхода введите q): ")
    if productInputData == 'q':
        break
    count += 1
    productInputData = productInputData.split(" ")
    print(productInputData)
    productData = {nameProductKey: productInputData[0], priceProductKey: productInputData[1],
                   countProductKey: productInputData[2]}
    product = (count, productData)
    productList.append(product)

nameProductList = []
priceProductList = []
countProductList = []
productInfo = {}
for item in productList:
    productData = item[1]
    nameProductList.append(productData[nameProductKey])
    priceProductList.append(productData[priceProductKey])
    countProductList.append(productData[countProductKey])
productInfo[nameProductKey] = nameProductList
productInfo[priceProductKey] = priceProductList
productInfo[countProductKey] = countProductList
print(productList)
print(productInfo)
