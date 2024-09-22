########## The first decision for task№2.1 ##########
user_num = input('Type your 4-digit number: ' )
print(user_num[0], user_num [1], user_num[2], user_num[3], sep= '\n')


########## The second decision for task№2.1 ##########
user_num = int(input('Type your 4-digit number: ' ))
num_1 = user_num // 1000
num_2 = (user_num  % 1000) // 100
num_3 = ((user_num % 1000) % 100) // 10
num_4 = ((user_num % 1000) % 100) % 10

print(num_1, num_2, num_3, num_4, sep='\n')