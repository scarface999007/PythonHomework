class Cell:
    def __init__(self, element):
        self.element = element

    def __add__(self, other):
        return Cell(self.element + other.element)

    def __sub__(self, other):
        if self.element > other.element:
            return Cell(self.element - other.element)
        elif self.element < other.element:
            return Cell(other.element - self.element)
        else:
            print("Разность ячеек двух клеток = 0")
            return Cell(None)

    def __mul__(self, other):
        return Cell(self.element * other.element)

    def __truediv__(self, other):
        return Cell(self.element // other.element)

    def make_order(self, cells_in_row):
        res = ""
        count = self.element
        temp_str = ""
        while count > 0:
            temp_str += '#'
            if len(temp_str) == cells_in_row:
                res += temp_str + '\n'
                temp_str = ""
            count -= 1
        res += temp_str
        return res
