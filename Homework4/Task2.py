"""
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента. Если ключ не хешируем,
используйте его строковое представление.
"""


def key_parameters_to_dict(**kwargs) -> dict:
    """A function that takes in only key parameters
    and returns a dictionary"""
    try:
        return dict(zip(kwargs.values(), kwargs.keys()))
    except TypeError:
        inverse_dic = {}
        for key, val in kwargs.items():
            inverse_dic[','.join(val)] = key
        return inverse_dic


print(key_parameters_to_dict(dog='1', cat='3'))
print(key_parameters_to_dict(dog=['1', '2'], cat=['3']))
