import time
from enum import Enum


class Color(Enum):
    RED = "Красный"
    YELLOW = "Жёлтый"
    GREEN = "Зелёный"


class TrafficLight:
    __color = Color.RED

    def running(self):
        print(self.__color.value)
        time.sleep(7)
        self.__color = Color.YELLOW
        print(self.__color.value)
        time.sleep(2)
        self.__color = Color.GREEN
        print(self.__color.value)

