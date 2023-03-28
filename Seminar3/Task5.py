my_list = [1, 1, 1, 1, 2, 2, 24, 4, 45, 5, 5, 7, 7, 2, 2, 24, 4, 4]
new_list = []
for i, item in enumerate(my_list, start=1):
    if item % 2 != 0:
        new_list.append(i)
print(new_list)
