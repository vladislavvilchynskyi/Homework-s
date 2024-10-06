import string

interval = input("Enter letters from 'a' to 'z' with '-': ")
print(string.ascii_letters[(string.ascii_letters.find(interval[0])) : (string.ascii_letters.find(interval[-1]) + 1)])
