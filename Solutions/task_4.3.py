user_numbers = input("Type your numbers: ")
user_list = list(user_numbers)

new_list = []
new_list.append(user_list[0])
new_list.append(user_list[2])
new_list.append(user_list[-2])

print(f'Your new list is {new_list}')