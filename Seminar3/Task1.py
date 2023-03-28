"""The quick way"""
init_list = [2, 3, 5, 2, 6, 10, 10]
unique_list = list(set(init_list))
print(unique_list)

"""The long way"""
init_list = [2, 3, 5, 2, 6, 10, 10]
unique_list = []
for i in init_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)
