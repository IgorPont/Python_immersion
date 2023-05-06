# class Archive:
#     my_list = list()
#
#     def __init__(self, number: int, string: str):
#         self.number = number
#         self.string = string
#         self.save()
#
#     def save(self):
#         self.my_list.append((self.number, self.string))
#
#
# if __name__ == '__main__':
#     instance_1 = Archive(1, 'text 1')
#     print(instance_1.my_list)
#     instance_2 = Archive(2, 'text 2')
#     print(instance_2.my_list)

class Archive:
    """
    Класс Архив, который хранит пару свойств: число и строку.
    При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются
    в пару списков-архивов. list-архивы также являются свойствами экземпляра.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_num = list()
            cls._instance.list_str = list()
        else:
            cls._instance.list_num.append(cls._instance.num)
            cls._instance.list_str.append(cls._instance.string)
        return cls._instance

    def __init__(self, num, string):
        self.num = num
        self.string = string

    def __str__(self):
        return f'Для пользователя: {self.list_num} {self.list_str}'

    def __repr__(self):
        return f'Для программиста: {self.list_num} {self.list_str}'


if __name__ == '__main__':
    instance_1 = Archive(1, 'text_1')
    print(instance_1.list_num, instance_1.list_str)
    instance_2 = Archive(2, 'text_2')
    print(instance_2.list_num, instance_2.list_str)
    # help(Archive)
    print(instance_1)
    print(repr(instance_2))

