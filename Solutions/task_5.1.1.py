import keyword
import string

def value_name(user_str):
        if not user_str.isidentifier():
            return False
        if any(char in string.punctuation.replace('_', '') for char in user_str):
            return False
        if user_str.count('_') > 1:
            return False
        if user_str in keyword.kwlist:
            return False
        if any(char.isupper() for char in user_str):
            return False
        return True


print(value_name("_"))                       # True
print(value_name("__"))                      # False
print(value_name("___"))                     # False
print(value_name("x"))                       # True
print(value_name("get_value"))               # True
print(value_name("get value"))               # False
print(value_name("get!value"))               # False
print(value_name("some_super_puper_value"))  # True
print(value_name("Get_value"))               # False
print(value_name("get_Value"))               # False
print(value_name("getValue"))                # False
print(value_name("3m"))                      # False
print(value_name("m3"))                      # True
print(value_name("assert"))                  # False
print(value_name("assert_exception"))