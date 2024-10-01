############################### STRING ###############################

# value_str = 'hello' # ітерований, ііндексований та незмінюваний тип даних.

# print(value_str[::-1]) # реверс строки
# print(value_str[::2]) # виводить кожний другий елемент

# value_str = 'email@gmail.com'
# value_lower_case = value_str.lower() #валідатор, покайока від неправильного вводу користувача
# # value_upper_case = value_str.upper() #валідатор, покайока від неправильного вводу користувача
#
# first_name = 'Vlad vi'
# # value_capital = first_name.capitalize() # Повертає ПЕРШЕ слово з усієї строки з великої літери
# # value_title = first_name.title() # Повертає КОЖНЕ слово з усіх введених з великої літери
# # value_swapcase = first_name.swapcase() # Повертає сторку з реверсивним регістром
#
# # print(value_title)
#
# value_str = ('12w')
# result = ''
#
# # for letter in value_str:
#     if letter.isdigit():
#         result += letter # так можна почитити рядок , щоб отримати число від юзера

# print(result)

value_str = 'helloloool'

# some_method = value_str.find('h') # шукає елмент та виводить його індекс
# some_method = value_str.rfind('ll') # шукає елемент з кінця списку

# if value_str.startswith('h'): # проверяет начинается ли строка с данного елемента
#     print(True)

# .endswith проверяет заканчиватесся ли строка данным елементом

#### split/join ####


some_file = "C/:My Computer/SomeFolder/file.png"
# split_method = some_file.split(".",1) # формирует лист относительно сепаратора, который мы укажем
#                                     # убирая сепараторный елемент, который мы укажем
#                                     # по дефолту дети по спейсу, если не вводить значение сепаратора
#
#
# split_method[1] = "jpeg"
# print(split_method, type(split_method))
#
# join_method = ".".join(split_method) # из листа делает опять данные которые мы меняли

# print(join_method)


# strip()

# first_name = '__Nick__'
# print(first_name.strip('_')) # удаляет указаные символы из списка (НЕ БУКВЫ)
# print(first_name.lstrip('_')) # удаляет указаные символы из начала списка (НЕ БУКВЫ)
# print(first_name.rstrip('_')) # удаляет указаные символы из конца списка (НЕ БУКВЫ)
#                             # по дефолту - убирает пробелы
#
#
# # .find()  выводит индекс елемента, который мы указали, но если мы указали несуществующий елемент - выведет -1
# # .index() выводит индекс елемента, который мы указали, но если мы указали несуществующий елемент - будет ошибка
#
#
#
# ################# ASCII #################
#
# value_str = 'hello'
# value_str_2 = 'hеllo'
# print(chr(39))
# print(ord("a"))
#
# alphabet = ""
#
# for letter in range(ord('a'), ord('z') + 1):
#     alphabet += chr(letter)
# print(alphabet)


import
