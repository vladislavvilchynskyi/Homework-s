while True:
    user_input = input("Введіть ціле число: ")
    if user_input.isdigit():
        result = int(user_input)
        break
    else:
        print("Будь ласка, введіть дійсне ціле число.")
while result > 9:
    final_number = 1
    for numb in str(result):
        final_number *= int(numb)
    result = final_number
print(result)