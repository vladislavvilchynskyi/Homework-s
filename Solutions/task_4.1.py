#database
list_1 = [0, 1, 0, 12, 3]
list_2 = [0]
list_3 = [1, 0, 13, 0, 0, 0, 5]
list_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


# example #1
count = list_1.count(0)
while 0 in list_1:
     list_1.remove(0)
     continue

count_2 = list_1.count(0)
while count_2 < count:
    list_1.append(0)
    count_2 += 1
print(list_1)


# example #2

count = list_2.count(0)
while 0 in list_2:
     list_2.remove(0)
     continue

count_2 = list_2.count(0)
while count_2 < count:
    list_2.append(0)
    count_2 += 1
print(list_2)


# example #3

count = list_3.count(0)
while 0 in list_3:
     list_3.remove(0)
     continue

count_2 = list_3.count(0)
while count_2 < count:
    list_3.append(0)
    count_2 += 1
print(list_3)


# example #4

count = list_4.count(0)
while 0 in list_4:
     list_4.remove(0)
     continue

count_2 = list_4.count(0)
while count_2 < count:
    list_4.append(0)
    count_2 += 1
print(list_4)

