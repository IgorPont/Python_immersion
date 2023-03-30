"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

initial_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6]
result_list = []
for i in initial_list:
    if initial_list.count(i) == 2:
        result_list.append(i)
result_list = list(set(result_list))
print(result_list)
