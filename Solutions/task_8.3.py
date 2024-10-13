def find_unique_value(some_list):

    count_dict = {}
    for item in some_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    for item, count in count_dict.items():
        if count == 1:
            return item

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")