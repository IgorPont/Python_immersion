init_list = [1, 1, 1, 1, 2, 2, 3, 3, 5, 6, 6]
new_list = []
for i in init_list:
    if init_list.count(i) != 2:
        new_list.append(i)
print(new_list)
