"""
3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
"""
from random import randint


def guess_number():
    num_required = randint(0, 1000)
    print(num_required)
    stroke_count = 10
    while stroke_count != 0:
        user_num = int(input('Enter a number:\n'))
        if user_num == num_required:
            print(f'Victory! You guessed the number!')
            break
        elif user_num > num_required:
            stroke_count -= 1
            print(f'You have entered too large a number\n{stroke_count} attempts left\n')
        else:
            stroke_count -= 1
            print(f'You have entered a number that is too small\n{stroke_count} attempts left\n')
    if stroke_count == 0:
        print('You have lost')
    return True


guess_number()
