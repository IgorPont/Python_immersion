import random

file_name = 'test1.txt'
COUNT_STRING = 5
MIN_NUM = -1000
MAX_NUM = 1000


def file_write(count_str: int, name_file: str) -> None:
    """..."""
    with open(name_file, 'a', encoding='utf-8') as f:
        for i in range(count_str):
            f.write(f'{random.randint(MIN_NUM, MAX_NUM)}|{random.uniform(MIN_NUM, MAX_NUM)}\n')


file_write(COUNT_STRING, file_name)
