# *args для добавления аргументов в функцию - возвращает в тупле
# **kwargs для добавления именных аргументов - возвращает словарь


# def draw_rectangle(w, h, fill):
#     for i in range(w):
#         for j in range(h):
#             print(fill, end='')
#
#     return None
#
# # пример аргса
# my_args = 5, 7,  "*"
#
# draw_rectangle(*my_args)



# def in list

# def my_add(num_1, num_2):
#     return num_1 + num_2
#
#
# def my_mul(num_1, num_2):
#     return num_1 * num_2
#
#
# calc_list = [my_add, my_mul]
#
# for my_func in calc_list:
#     print(my_func(2, 3))



### def in def

# def my_add(num_1):
#     return num_1 + 2
#
#
# def my_mul(num_1):
#     return num_1 * 2
#
#
# def my_calc(num_list, func):
#     for num in num_list:
#         print(func(num))
#
# my_calc([1, 2, 3, 4], my_mul)





###### додаткові методи стрінги
# .__doc__
# .__name__
# .__module__
#
# def my_func():
#     return 10
#
# if __name__ == "__main__":
#     print(my_func.__doc__)
#     print(my_func.__name__)
#     print(my_func.__module__)



########### lambda function ###########
#
# def my_filter(seq, predicate):
#     result = []
#
#     for el in seq:
#         if predicate(el):
#             result.append(el)
#
#     return result
#
#
# def greater_than_zero(x):
#     return x > 0
#
#
# sequence = [0, 9, 8, -4, 2]
#
# print(my_filter(sequence, greater_than_zero))
#
# # АБО через лямбду, lambda - це проста функція, яку можемо вписати для переврінки чогось, елементарні речі
#
# print (my_filter(sequence, lambda x: x > 0))
# # можна покласти лямбду в змінун і викликати цю змінну багато разів в коді
#


####### map(), filter(), zip()

### map() - генерує ряд елементів, до яких було застосовано якусь функцію
#
#
# sequence = [1, 2, 0, -4, 5, 6, -1]
#
#
# def to_int(func, seq):
#     result = []
#     for i in seq:
#         result.append(func(i))
#     return result
# # OR
# new_seq = map(int, sequence)
# print(new_seq)
# print(list(new_seq))


## filter() сортує елементи за правилом, і виводить нам відсотрований об'єкт

# filter_nums = filter(lambda x: x > 0, sequence)
# print(list(filter_nums))



## zip() сортує наші ітеровані об'єкти по найменшій довжині одного з об'єктів

sequence_1 = [1, 2, 0, -4, 5, 6, -1]
sequence_2 = ['apple', 'red', "gold", 'good']
sequence_3 = [True, False, None]

for elements in zip(sequence_1, sequence_3, sequence_2):
    print(elements)
