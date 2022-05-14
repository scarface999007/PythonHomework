class Road:
    _mass = 25
    _thickness = 5
    __res = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass_calc(self):
        self.__res = self._length * self._width * self._mass * self._thickness
        print(str(self._width) + " м*" + str(self._length) + " м*" + str(self._mass) + " кг*" + str(
            self._thickness) + " см = " + str(int(self.__res/1000)) + " т")
