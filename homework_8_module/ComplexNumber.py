class ComplexNumber:
    def __init__(self, real_num, imaginary_num):
        self.real_num = real_num
        self.imaginary_num = imaginary_num

    def __add__(self, other):
        return ComplexNumber(self.real_num + other.real_num, self.imaginary_num + other.imaginary_num)

    def __mul__(self, other):
        return ComplexNumber(self.real_num * other.real_num - self.imaginary_num * other.imaginary_num,
                             self.imaginary_num * other.real_num + self.real_num * other.imaginary_num)

    def __str__(self):
        return str(self.real_num) + " + " + str(self.imaginary_num) + "i"
