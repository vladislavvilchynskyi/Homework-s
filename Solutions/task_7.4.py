def common_elements():
    set_3 = set()
    set_5 = set()
    for i in range(0, 100):
        if i % 5 == 0:
            set_5.add(i)
        if i % 3 == 0:
            set_3.add(i)

    final_set = set_5.intersection(set_3)
    return final_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")