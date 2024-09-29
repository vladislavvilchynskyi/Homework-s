#database
list_1 = [1, 3, 5]
list_2 = [6]
list_3 = []



#example #1

summary = 0
if len(list_1) > 0:
    for index, value in enumerate(list_1):
        if index % 2 == 0:
            summary += value
    summary = summary * list_1.pop(-1)
    print(f'Your summary is {summary}')
else:
    print(summary)


# example #2

summary = 0
if len(list_2) > 0:
    for index, value in enumerate(list_2):
        if index % 2 == 0:
            summary += value
    summary = summary * list_2.pop(-1)
    print(f'Your summary is {summary}')
else:
    print(summary)


# example #3

summary = 0
if len(list_3) > 0:
    for index, value in enumerate(list_3):
        if index % 2 == 0:
            summary += value
    summary = summary * list_3.pop(-1)
    print(f'Your summary is {summary}')
else:
    print(f'Your summary is {summary}')
