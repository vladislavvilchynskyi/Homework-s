from msilib import add_data


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def add_square(self, other):
        return self.get_square() + other.get_square()

    def mul_square(self, n):
        return self.get_square() * n

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        add_square = self.get_square() + other.get_square()
        return Rectangle(self.width, add_square / self.width)

    def __mul__(self, n):
        mul_square = self.get_square() * n
        return Rectangle(self.width, mul_square / self.width)

    def __str__(self):
        return f'Bro, It`s your new Rectangle:\nWidth: {self.width}\nHeight: {self.height}\nSee you later :*\n\n'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
print(r1)
print(r2)
print(r3)
print(r4)
assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
