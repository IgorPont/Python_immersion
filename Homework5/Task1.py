"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def path_to_tuple(link: str) -> tuple[str, str, str]:
    """A function that splits the file path into a tuple"""
    *_, file_name = link.split('/')
    *_, extension = file_name.split('.')
    tuple_link = (link, file_name, extension)
    return tuple_link


print(path_to_tuple(link='C:/Users/igor/Downloads/test.txt'))
