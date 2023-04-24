import random
from typing import Callable


def deco(func: Callable) -> Callable[[], None]:
    min_number = 1
    max_number = 100
    min_count = 1
    max_count = 10

    def wrapper(number: int, number_attempts: int, *args, **kwargs):
        if not min_number <= number <= max_number:
            number = random.randint(min_number, max_number)
        if not min_count <= number_attempts <= max_count:
            number_attempts = random.randint(min_count, max_count)

        result = func(number, number_attempts)

    return wrapper


@deco
def guess_number(number: int, number_attempts: int):
    print(f'Guess the number in {number_attempts} tries')
    for i in range(number_attempts):
        user_num = int(input(f'Enter the number: '))
        if user_num == number:
            print(f'Win!')
            break
        elif user_num < number:
            print(f'The number you have in mind is greater than')
        else:
            print(f'The number you have in mind is less than')
    else:
        print(f'Lost. The number that was guessed is {number= }, {number_attempts= }')


if __name__ == '__main__':
    guess_number(1000, 15)
