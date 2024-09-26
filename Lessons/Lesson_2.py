#DataTypes


#....................Anmutable.......................
#int() 10
#float() 10.5 округулює числа
#decinal 10.5 більш точне число (опціонально) при точних розрахунках використовуємо лише даний тип даних!
#complex() (1 + 2j)

#str() рядок

#tuple кортеж
#bool Логічний оператор (True/False) (0/1)
#None відстуність будь якого значення


#................Mutable..................
#list() список
#dict() словник
#set() множини


# ......Змінна......

num_1 = 345

#id() Показує нам номер комірки в якій зберігаються наші данні
#type() Показує нам тип (клас)

num_1 = 2
##print(num_1, id(num_1), type(num_1))

#Math operation
num_1 = 11
num_2 = 2

multi_result = divmod(num_1, num_2) #ця ф-ція повертає нам одночасно 2 значення - цілочисленне ділення та залишок від ділення)
##print(multi_result,type(multi_result))

#Concatenation or f_string?

name = 'Vlad'
surname = 'Vilchynskyi'
age = 25

full_name = name + ' ' + surname
age_name = f"My name is {name} I'm {age} old"
print(full_name, age_name, end='! ')



