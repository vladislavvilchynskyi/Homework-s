

while True:

    num_1 = float(input("Type your first number: "))
    operation = input("Choice and type the operation what you want to do  / , *, + or - : ")
    num_2 = float(input("Type your second number: "))
    if num_2 == 0 and operation == "/":
        print("Oh Bro I`m sorry, but cannot be divided by zero!", "Please, type another number, thanks:)", sep='\n')
        num_2 = float(input("Type your second number: "))


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

    next = input("If you want to exit the calculator, enter - n, otherwise, enter - y: ")
    if next == "y":
        continue
    else:
        break