import string

user_string = input("Enter your string: ")
hashtag = user_string.title()
hashtag = hashtag.split(" ")
hashtag = "".join(hashtag)
for element in string.punctuation:
    hashtag = hashtag.split(element)
    hashtag = "".join(hashtag)
if len(hashtag) > 140:
    print(hashtag[:141])
else:
print(f'#{hashtag}')
