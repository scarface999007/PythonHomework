# 1. Поработайте с переменными, создайте несколько, выведите на экран.
#    Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

i = 1
isEnabled = True
print(i)
print(isEnabled)

userName = input("1. Введите имя пользователя: ")
userAge = input("1. Введите возраст пользователя: ")
print("Имя: " + userName)
print("Возраст: " + userAge)

# 2. Пользователь вводит время в секундах.
#    Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
#    Используйте форматирование строк.

timeInSeconds = int(input("2. Введите время в секундах: "))
hours = str(timeInSeconds // 3600)
remainSeconds = timeInSeconds % 3600
minutes = str(remainSeconds // 60)
seconds = str(remainSeconds % 60)

if len(hours) == 1:
    hours = "0" + hours

if len(minutes) == 1:
    minutes = "0" + minutes

if len(seconds) == 1:
    seconds = "0" + seconds

time = hours + ":" + minutes + ":" + seconds

print(time)

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#    Например, пользователь ввёл число 3.
#    Считаем 3 + 33 + 333 = 369.

num = input("3. Введите число: ")
doubleNum = num + num
tripleNum = doubleNum + num

concatNum = int(num) + int(doubleNum) + int(tripleNum)
print("Сумма чисел: " + str(concatNum))

# 4. Пользователь вводит целое положительное число.
#    Найдите самую большую цифру в числе.
#    Для решения используйте цикл while и арифметические операции.

num = input("4. Введите число: ")
numLen = len(num) - 1
maxNum = 0
while numLen >= 0:
    digit = int(num[numLen])
    if digit > maxNum:
        maxNum = digit
    numLen -= 1
print("Самая большая цифра: " + str(maxNum))

# 5. Запросите у пользователя значения выручки и издержек фирмы.
#    Определите, с каким финансовым результатом работает фирма.
#    Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
#    Выведите соответствующее сообщение.

revenue = int(input("Выручка: "))
expenses = int(input("Издержки: "))
isRevenue = revenue > expenses
if isRevenue:
    print("Прибыль")
else:
    print("Убыток")

# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
#    Это отношение прибыли к выручке.
#    Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

if isRevenue:
    profit = revenue - expenses
    revenueProfitability = profit / revenue
    employee = int(input("Введите количество работников: "))
    print("Прибыль фирмы в расчёте на одного сотрудника: " + str(revenueProfitability / employee))

# 7. Спортсмен занимается ежедневными пробежками.
#    В первый день его результат составил a километров.
#    Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
#    Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
#    Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

firstResult = int(input("Введите первый результат: "))
targetResult = int(input("Введите целевой результат : "))
day = 1

progress = firstResult
print("День " + str(day) + ": " + str(progress))
while progress <= targetResult:
    progress += progress * 0.1
    day += 1
    print("День " + str(day) + ": " + str(progress))
