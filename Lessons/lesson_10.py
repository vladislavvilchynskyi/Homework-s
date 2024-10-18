################################### GENERATOR ###################################

# def add_one(num):
#     return num + 1
#
#
# def count(start, func):
#     while True:
#         yield start  # yield - ставить цикл на паузу ы починаэ його настпноъ строки, не з початку циклу
#         start = func(start)
#
# counter = count(0, add_one)
#
# print(next(counter))
# print(next(counter))  # next - запускає yield з того місця де ми зупинились
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))



# def some_gen():
#     yield 42
#
# gen = some_gen()
# print(gen)
# print(list(gen))
# print(list(gen)) # з генератора можна створити ліст, генератор НЕ ЗБЕРІГАЄ ВСІ ДАНІ, він бере 1-не значення і ддає його нам, замінюючи в пам'яті його настпним значенням


# def s_gen():
#     x = 1
#     while x > 0:
#         x = yield 45
#         print(f'Receiving {x}')
#         if x is None:
#             x = 0
#
# new_val = s_gen()
# print(next(new_val))
# new_val.send(90)    # send - задаэ значення для yield, тобто ми можемо покласти значення у "ілд" і не важливо де він знаходиться
# print(next(new_val))



# value_list = (i * 2 for i in range(5))  # це запис генератору, генератор запам'ятовує УМОВУ і лише 1 значення, яке віддає і заміняє на нове, доки не віддасть
#
# print(value_list)
# print(next(value_list))
# print(next(value_list))
# print(next(value_list))
# print(next(value_list))
# print(next(value_list))
# print(next(value_list))
# print(next(value_list))



##### closures ( замикання) #####
# def calculate_pow(n):
#
#     def calculate(number):
#         print(locals())
#
#         return number ** n
#
#     return calculate
#
# f = calculate_pow(3)
# f_2 = calculate_pow(2)
#
# print(f) # покажчик на вкладену ф-ію
# number_0ne = f(2) # виклик вкладеної ф-ії
# number_two = f_2(5)
# print(number_0ne)
# print(number_two)






############################ decorators ############################
# приклад для чого може знадобитися - людина ходить по сайту, треба трекати постійно які в тебе дозволи, залогінений ти чи не і тд
# декоратор - це шось, що обвалаківаєт нашу функцію, не змінюючи її





