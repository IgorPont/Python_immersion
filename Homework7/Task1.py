"""
Напишите функцию группового переименования файлов.
Она должна:
- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
- принимать параметр количество цифр в порядковом номере.
- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
- принимать параметр расширение конечного файла.
- принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""

import os
from pathlib import Path


def group_rename(new_filename: str, serial_number: int, old_extension: str,
                 new_extension: str, old_filename_range: list[int]) -> None:
    """Group file renaming function"""
    count = 0
    for file in os.listdir():
        if file.endswith(old_extension):
            count += 1
            Path(file).rename(
                f"{file.split('.')[0][old_filename_range[0]:old_filename_range[1]]}"
                f"{new_filename}{count:0>{serial_number}}.{new_extension}"
            )


if __name__ == '__main__':
    group_rename('new_name', 3, 'txt', 'pdf', [2, 4])
