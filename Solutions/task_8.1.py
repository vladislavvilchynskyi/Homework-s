def add_one(some_list):
    some_list = ''.join(map(str,some_list))
    value = int(some_list) + 1
    some_list_2 = []
    for digit in str(value):
        some_list_2.append(int(digit))
    return some_list_2




assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")


