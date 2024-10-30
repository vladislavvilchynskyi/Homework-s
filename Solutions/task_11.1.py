def prime_generator(end):
    def simple_digit (value):
        if value <= 1:
            return False
        for i in range(2, int(value ** 0.5) + 1):
            if value % i == 0:
                return False
        return True

    for num in range(2, end + 1):
        if simple_digit(num):
            yield num


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')