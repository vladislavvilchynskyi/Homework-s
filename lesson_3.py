########### bool ##########

#булєві змінні краще називати питанням, на яке ти хочеш відповісти
#is_true = False
#is_confirmed = True


#value_int = 0 # якщо в нас значення дорівнює "0"завжди буде False, інше будь яке значення - True
#value_float = 0 # Аналогічно цілим числам, але якщо число нескінченно мале то також будемо мати - False
#value_str = " " # False лише тоді коли немає символів в рядку - "", все інше - True

#приклад "утіной тіпізаціі"
#value_bool = True
#print(value_bool * 10)

########### logic operator ########### >,<,>=,<=,==,!=,in,not,is
#value_int_1 = 1000
#value_int_2 = 10

#print(value_int_1 > value_int_2)

#print("He" in "Hello") #зручно шукати елементи в списках і тд.
#print('He' not in "Hello")

value_int = 1
value_float = 1.0
#print(value_int == value_float)
#print(value_int is value_float) #перевіряє чи дивляться змінні на одну комірку пам'яті чи ні





#if умова:
#     роби це (виконання)
if value_int > 0 and value_int > 1: # так по людски (для гуманитариев)
#if 0 < value_int > 1: # так по PEP8
    print(f'{value_int} is True')
elif value_int < 3:
    print(f'{value_int} is not bigger')
else:
    print("is not your value :(")



if value_int > 0 or value_int > 1: # так по людски (для гуманитариев)
#if 0 < value_int > 1: # так по PEP8
    print(f'{value_int} is True')
elif value_int < 3:
    print(f'{value_int} is not bigger')
else:
    print("is not your value :(")

####################### list #######################
some_list = [1,2,'hello', True, 0.5]
#some_list = list() #так можна создать список
print(id(some_list))
print(some_list[1])
print(some_list[-1])
print(some_list[1:3])
print(some_list[:2])
print(some_list[2:])
print(some_list[0:5:2])








