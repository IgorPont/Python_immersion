"""
2. Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""


def prime_number(num):
    res = None
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                res = f'{num} is not a prime number'
                break
        else:
            res = f'{num} is a prime number'
    else:
        res = f'{num} is not a prime number'
    return res


def get_number():
    while True:
        res = int(input('Enter a number to check if it is prime:\n'))
        if res > 0 and res <= 100000:
            break
        else:
            print('Invalid number')
    return res


print(prime_number(get_number()))
