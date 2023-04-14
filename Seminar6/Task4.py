from Task3 import guess, save, journal


def function():
    dict_ = {'Зимой и летом одним цветом': ['елка', 'ель', 'ёлка'],
             'Висит груша - нельзя скушать': ['лампочка'],
             'Зимой белый, летом серый': ['заяц'], }
    for question, answer in dict_.items():
        guess(question, answer, 3)


if __name__ == '__main__':
    function()
