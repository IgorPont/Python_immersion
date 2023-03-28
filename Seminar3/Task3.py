my_tuple = ('str1', 'str2', True, False, 11, 28, [1, 2, 3], {1: 1, 2: 2, }, (23, 45))
my_dict = {}
for entity in my_tuple:
    # возвращает все значения конкретного типа (параметра) и помещает в список
    res = my_dict.setdefault(type(entity), [])
    res.append(entity)
print(my_dict)
