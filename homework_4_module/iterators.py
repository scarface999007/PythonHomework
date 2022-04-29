from itertools import count
from itertools import cycle


def iterator_to_100(num):
    for el in count(num):
        if el > 100:
            break
        else:
            print(el)


def repeat_iterator(item_list):
    item_count = 0
    for el in cycle(item_list):
        if item_count >= len(item_list):
            break
        print(el)
        item_count += 1


def fact(num):
    res = 1
    for el in range(1, num + 1):
        res *= el
        yield res
