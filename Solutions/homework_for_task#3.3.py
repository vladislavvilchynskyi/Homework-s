
import math

list_1 = [1, 2, 3]
list_2 = [1, 2, 3, 4, 5, 6]
list_3 = [1, 2, 3, 4, 5]
list_4 = [1]
list_5 = []


# example #1

left_list = []
right_list = []
len_list = len(list_1)
if len_list % 2 == 0:
    index_1 = int(len_list // 2)
    left_list = list_1[:index_1]
    right_list = list_1[index_1:]
elif len_list % 2 != 0:
    index_2 = math.ceil(int(len_list // 2))
    index_2 = index_2 + 1
    left_list = list_1[:index_2]
    right_list = list_1[index_2:]

final_list = [left_list , right_list]
print(final_list)


# example #2

left_list = []
right_list = []
len_list = len(list_2)
if len_list % 2 == 0:
    index_1 = int(len_list // 2)
    left_list = list_2[:index_1]
    right_list = list_2[index_1:]
elif len_list % 2 != 0:
    index_2 = math.ceil(int(len_list // 2))
    index_2 = index_2 + 1
    left_list = list_2[:index_2]
    right_list = list_2[index_2:]

final_list = [left_list , right_list]
print(final_list)


# example #3

left_list = []
right_list = []
len_list = len(list_3)
if len_list % 2 == 0:
    index_1 = int(len_list // 2)
    left_list = list_3[:index_1]
    right_list = list_3[index_1:]
elif len_list % 2 != 0:
    index_2 = math.ceil(int(len_list // 2))
    index_2 = index_2 + 1
    left_list = list_3[:index_2]
    right_list = list_3[index_2:]

final_list = [left_list , right_list]
print(final_list)


# example #4

left_list = []
right_list = []
len_list = len(list_4)
if len_list % 2 == 0:
    index_1 = int(len_list // 2)
    left_list = list_4[:index_1]
    right_list = list_4[index_1:]
elif len_list % 2 != 0:
    index_2 = math.ceil(int(len_list // 2))
    index_2 = index_2 + 1
    left_list = list_4[:index_2]
    right_list = list_4[index_2:]

final_list = [left_list , right_list]
print(final_list)

# example #5

left_list = []
right_list = []
len_list = len(list_5)
if len_list % 2 == 0:
    index_1 = int(len_list // 2)
    left_list = list_5[:index_1]
    right_list = list_5[index_1:]
elif len_list % 2 != 0:
    index_2 = math.ceil(int(len_list // 2))
    index_2 = index_2 + 1
    left_list = list_5[:index_2]
    right_list = list_5[index_2:]

final_list = [left_list , right_list]
print(final_list)