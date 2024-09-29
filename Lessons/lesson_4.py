# альтернатива іф еліф, читабельно, для простих перевірок, погана швидкодія

weather = "hot"

match weather:
    case "cold":
        print("It`s cold")
    case "rainy":
        print("It`s rainy")
    case "hot":
        print('It`s hot')
    case "snowy":
        print('It`s snowy')

################ LIST ################

my_list = [1, 2, 3]

my_list.append("hello") #додає елемент у кінець списку
                        #цей метод нічого не повертає,
                        # відповідно не потребує присвоєння до нової змінної.


my_list.pop()          #видаляє значення за індексом і зберігає данні, які видалив, тобто їх можна загнати в змінну.


my_list.insert(99, "hello")  #вставляє дані у певний індекс ліста,
                                            # якщо цього індексу ще немає в списку, просто ставить на саме останнє місце


my_list.reverse()       #перевертає список
my_list_2 = my_list[::-1]  #копіює і перевертає список, майже теж саме, але займає па'мять і не такий швидкодіючий.


my_list.sort(reverse=False, key=bool)  #сортує по ключу.
some_list = sorted(my_list, reverse=False, key=bool)  #копіює сортований список ну і сортує


print(my_list)



############### LOOP цикли ###############

# value_int = 0
# is_true = True
#
# # while True:
# #     value_int += 1
# #     print(value_int)
#
# # while value_int < 10:
# #     value_int += 1
# #     print(value_int)
#
# while is_true:
#     value_int += 1
#     if value_int == 5:
#         continue            # воно не пускає тебе далі по коду, те що під контінью не виконується
#     print(value_int)
#
#     if value_int >= 10:
#         is_true = False
#
# # while True:
# #     value_int += 1
# #     print(value_int)
# #     if value_int >= 10:
# #         break
# else:
#     print("ha-ha-ha")
#
# print("end")

value_str = "hello"

index = 0
while index < len(value_str):
    print(value_str[index])
    index += 1

for letter in value_str:
    print(letter)
    break
else:
    print("lflflflfl")

#range()
# range(5) від 0 до 4 включно ( 5 не входить!)
# range(2, 5) від 2 до 4 включно
# range(2, 5, 2) від 2 до 4 включно з кроком 2
