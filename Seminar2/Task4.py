from decimal import *
import decimal
from math import pi

decimal.getcontext().prec = 42  # установили количество знаков после запятой для decimal

PI = Decimal(pi)


def length_area_circle(diameter: Decimal) -> tuple[Decimal, Decimal]:
    return (PI * diameter,
            PI * (diameter / 2) ** 2)


def main():
    diam = 0
    while True:
        try:
            diam = Decimal(input('Enter diametr: '))
        except InvalidOperation:
            print('Enter a number')
        if not 0 < diam <= 1000:
            print('Enter a number between 0 and 1000')
        else:
            break

    leng, square = length_area_circle(diam)
    print(f'{leng=}, {square=}')


if __name__ == '__main__':
    main()
