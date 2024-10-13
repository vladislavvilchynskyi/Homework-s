import string
def is_palindrome(text):
    text = text.lower()
    cleared_text = ''
    for numb in text:
        if numb.isalnum():
            cleared_text += numb

    return cleared_text == cleared_text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")