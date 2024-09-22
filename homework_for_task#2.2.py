user_num = int(input('Type your 5-digit number: ' ))
num_1 = user_num % 10
num_2 = (user_num // 10) % 10
num_3 = ((user_num % 10000) % 1000) // 100
num_4 = (user_num % 10000) // 1000
num_5 = user_num // 10000
print(num_1, num_2, num_3, num_4, num_5, sep='')
