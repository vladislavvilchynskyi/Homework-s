import keyword
import string

num_all = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
user_string = input("Enter your value: ")
# if user_string not in keyword.kwlist:
#     if user_string not in string.punctuation:
#         if user_string.startswith(num_all):
#             print(False)
#         else:
#             if user_string.islower():
#                 print(True)
#             else:
#                 print(False)
#     elif user_string == "_":
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)
for i in user_string:
    list_1 = keyword.kwlist
    if i == user_string.isdigit():
        print(False)
    elif i == string.punctuation:
        print(False)
    elif i



