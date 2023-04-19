import random

file_name = 'test1.txt'
COUNT_STRING = 5
MIN_NUM = -1000
MAX_NUM = 1000


def file_write(count_str: int, name_file: str) -> None:
    """A function that fills a file with random pairs of integers and real numbers"""
    with open(name_file, 'a', encoding='utf-8') as f:
        for i in range(count_str):
            f.write(f'{random.randint(MIN_NUM, MAX_NUM)}|{random.uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == '__main__':
    file_write(COUNT_STRING, file_name)
