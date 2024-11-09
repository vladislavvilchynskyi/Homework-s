import math
from math import lcm

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def float_fraction(self):
        return self.a * self.b

    def common_denominator(self, other):
        return self.b * other.b

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        if self.b == other.b:
            return Fraction(self.a + other.a, self.b)
        else:
            common_denominator = self.common_denominator(other)
            a = self.a * other.b + other.a * self.b
            return Fraction(a, common_denominator)


    def __sub__(self, other):
        if self.b == other.b:
            return Fraction(self.a - other.a, self.b)
        else:
            common_denominator = self.common_denominator(other)
            a = self.a * other.b - other.a * self.b
            return Fraction(a, common_denominator)

    def __eq__(self, other):
        first = self.a / self.b
        second = other.a / other.b
        if first == second:
            return True
        else:
            return False

    def __gt__(self, other):
        first = self.a / self.b
        second = other.a / other.b
        if first > second:
            return True

    def __lt__(self, other):
        first = self.a / self.b
        second = other.a / other.b
        if first < second:
            return True
        else:
            return False

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
