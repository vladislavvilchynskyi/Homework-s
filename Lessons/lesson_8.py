# ############# function #############
# # рівень абстракції - це функція в функції , ієрархія функцій один в одній
# def adding_numbers(num_1, num_2):
#
#     if num_1 == 0:
#         result = 'error'
#         return result
#     else:
#         result = num_1 + num_2
#         return result
# print(adding_numbers(1,4))
#
# ##### види змінних
#     LEGB
#     local внутнішня
#     enclosing
#     global
#     built-in вбудована

from math import pi

# pi = "global"
#
# def outer():
#     pi = "enclosing"
# #    global pi вбудована функція, щоб обїявити глобальну функцію
#     def inner():
#         pi = 'local'
#         print(pi)
#
#     inner()
#
# outer()
# print(pi)

# def adding_numbers(num_1, num_2):
#
#     if num_1 != 0:
#         result = num_1 + num_2
#     print(locals()) # виводить нам словник з локальними ф-іями ( ключ : значення)
#     return result
# print(adding_numbers(9,13))
#


# true calculator
# import operator
#
# actions = {
#     '+': operator.add,
#     '-': operator.sub,
#     '*': operator.mul,
#     '/': operator.truediv,
# }
#
#
# num_1 = float(input("num_1 "))
# action = input("action ")
# num_2 = float(input('num_2 '))
# my_func = actions.get(action)
# if my_func:
#     print(my_func(num_1,num_2))
# # else:
# #     print('ERROR')
#
#
# ############# arguments #############
#
# IS_TRUE_EMAIL = True
#
# def print_line(fill, width, is_email=False):  #заповнення, довжина або к-сть
#     # дефолтний аргумент - is_email, це типу вимикача
#     for i in range(width):
#         print(fill, end='')
#
#     if is_email:
#         print('send email')

#print_line('*',6) #почерговий виклик
# print_line(width=6,fill='*')   #or ми використаємо іменований виклик і нам буде все одно в якому порядку давати значення
# print_line('*', width=6, is_email=False) #важлива черговысть
#print_line('*', width=6, is_email=IS_TRUE_EMAIL) #важлива черговысть

################### *args ###################

# def print_line(*args): #важливо ставити зірочку, називати можна як завгодно, але краще арг - це коли ми хлчемо взяти багато аргументів
#     return args
# print(print_line(1, 3, 3,))

################## kwargs ###################




##### annotation ###########
# Это для удобства пишем что мы хотим сюда получать

#
# def create_group(num_1: int, num_2: int) -> int:
#     return num_1 + num_2
#
# print(create_group(8, 9))
