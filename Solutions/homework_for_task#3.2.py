user_numbers = input("Type your numbers: ")
user_list = list(user_numbers)
num_1 = user_list[-1]
user_list.pop(-1)
user_list.insert(0,num_1)
print(user_list)
