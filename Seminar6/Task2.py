from random import randint
from sys import argv  # модуль для работы с терминальной строкой


def guess_the_number(min_: int, max_: int, attempts: int) -> bool:
    """The module generates a random number in a selected range and tries to guess the number"""
    number = randint(min_, max_)
    for i in range(attempts):
        guess = int(input('Input your guess: '))
        if guess < number:
            print('Small')
            continue
        elif guess > number:
            print('Big')
            continue
        else:
            return True
    return False


# Запускаем через терминал командой python3 Task2.py 1 10 5 (через пробел передаем параметры в функцию)
if __name__ == "__main__":
    print(guess_the_number(1, 8, 5))
    name, *args = argv
    print(guess_the_number(*(int(x) for x in
                             args)))  # Запускаем через терминал командой python3 Task2.py 1 10 5 (через пробел передаем параметры в функцию)
