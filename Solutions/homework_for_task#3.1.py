num_1 = float(input("Type your first number: "))
num_2 = float(input("Type your second number: "))
operation = input("Choice and type the operation what you want to do  / , *, + or - : ")

if num_2 == 0 and operation == "/":
    print("Oh Bro I`m sorry, but cannot be divided by zero!", "Please, type another number, thanks:)", sep='\n')
    num_2 = float(input("Type your second number: "))

#   float обрав тому що таким чином калькулятор не буде видавати помилку,
#   в разі як юзер захоче провести операції над нецілими числами,
#   якщо буде перетворення в int - буде обрізаний калькулятор

if operation == "/":
    result = num_1 / num_2
    print(f'Your result is: {result}')
elif operation == "*":
    result = num_1 * num_2
    print(f'Your result is: {result}')
elif operation == "+":
    result = num_1 + num_2
    print(f'Your result is: {result}')
elif operation == "-":
    result = num_1 - num_2
    print(f'Your result is: {result}')
