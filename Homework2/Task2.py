"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте модуль fractions.
"""
import fractions
import math


class RationalNumber:
    """Class rational number"""

    def __init__(self, numerator: int, denominator: int):
        self.__numerator = numerator
        self.__denominator = denominator

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def __str__(self):
        return f'{self.__numerator}/{self.__denominator}'

    def add_fractions(self, numerator2: int, denominator2: int) -> str:
        """Adding fractions"""
        if self.__denominator == denominator2:
            sum_numerators = self.__numerator + numerator2
            nod = math.gcd(sum_numerators, self.__denominator)
            if (self.__denominator // nod) == 0 or (self.__denominator // nod) == 1:
                return f'{sum_numerators // nod}'
            else:
                return f'{sum_numerators // nod}/{self.__denominator // nod}'
        else:
            # Find the least common multiple of
            nok = (self.__denominator * denominator2) // math.gcd(self.__denominator, denominator2)

            # Adding fractions
            common1 = nok // self.__denominator
            common2 = nok // denominator2
            sum_numerators = self.__numerator * common1 + numerator2 * common2
            nod = math.gcd(sum_numerators, nok)
            if (nok // nod) == 0 or (nok // nod) == 1:
                return f'{sum_numerators // nod}'
            else:
                return f'{sum_numerators // nod}/{nok // nod}'

    def multiply_fractions(self, numerator2: int, denominator2: int) -> str:
        """Multiplication of fractions"""
        multi_numerators = self.__numerator * numerator2
        multi_denominators = self.__denominator * denominator2
        nod = math.gcd(multi_numerators, multi_denominators)
        if (multi_denominators // nod) == 0 or (multi_denominators // nod) == 1:
            return f'{multi_numerators // nod}'
        else:
            return f'{multi_numerators // nod}/{multi_denominators // nod}'


def input_valid_num(message: str) -> int:
    """Checking input for validity"""
    if message.isdigit():
        return int(message)
    else:
        input_valid_num(input('Enter the number: '))


def test_add_fractions(verifiable: str,
                       numerator1: int, denominator1: int,
                       numerator2: int, denominator2: int):
    """Test of correct addition of fractions"""
    fraction1 = fractions.Fraction(numerator1, denominator1)
    fraction2 = fractions.Fraction(numerator2, denominator2)
    sum_ = fraction1 + fraction2
    if fractions.Fraction(verifiable) == sum_:
        print(f'The operation with fractions is correct!\n'
              f'The right result: {sum_}')
    else:
        print(f'Error! The right result: {sum_}')


def test_multiply_fractions(verifiable: str,
                            numerator1: int, denominator1: int,
                            numerator2: int, denominator2: int):
    """Test for correct multiplication of fractions"""
    fraction1 = fractions.Fraction(numerator1, denominator1)
    fraction2 = fractions.Fraction(numerator2, denominator2)
    mult = fraction1 * fraction2
    if fractions.Fraction(verifiable) == mult:
        print(f'The operation with fractions is correct!\n'
              f'The right result: {mult}')
    else:
        print(f'Error! The right result: {mult}')


def programme():
    """Fraction addition and multiplication program"""
    user_numerator1 = input_valid_num(input('Enter the numerator of the first number: '))
    user_denominator1 = input_valid_num(input('Enter the denominator of the first number: '))
    fraction1 = RationalNumber(user_numerator1, user_denominator1)
    print(fraction1)

    user_numerator2 = input_valid_num(input('Enter the numerator of the second number: '))
    user_denominator2 = input_valid_num(input('Enter the denominator of the second number: '))
    fraction2 = RationalNumber(user_numerator2, user_denominator2)
    print(fraction2)

    result_adding = fraction1.add_fractions(fraction2.get_numerator(), fraction2.get_denominator())
    print(f'{fraction1} + {fraction2} = {result_adding}')
    test_add_fractions(result_adding, fraction1.get_numerator(), fraction1.get_denominator(),
                       fraction2.get_numerator(), fraction2.get_denominator())

    result_multi = fraction1.multiply_fractions(fraction2.get_numerator(), fraction2.get_denominator())
    print(f'{fraction1} * {fraction2} = {result_multi}')
    test_multiply_fractions(result_multi, fraction1.get_numerator(), fraction1.get_denominator(),
                            fraction2.get_numerator(), fraction2.get_denominator())


if __name__ == '__main__':
    programme()
