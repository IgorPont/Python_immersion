"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


class ConvertToHex:
    """Convert a number to hexadecimal notation"""

    # The system of calculus
    BASE = 16
    # String representation of decimal numbers from 10 to 15 in hexadecimal
    STR_HEX = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

    def __init__(self, num):
        self.__num = num
        self.__hex = ''

    def get_num(self):
        return self.__num

    def __str__(self):
        return f'{self.__num} in hexadecimal system is {self.__hex}'

    def convert_num(self, num: int) -> str:
        """Method for converting a decimal to hexadecimal number"""
        res = ''
        while num > 0:
            temp = num % ConvertToHex.BASE
            if temp in ConvertToHex.STR_HEX:
                self.__hex += ConvertToHex.STR_HEX[temp]
            else:
                self.__hex += str(temp)
            num //= ConvertToHex.BASE
        self.__hex = self.__hex[::-1]
        return res


def input_valid_num(message: str) -> int:
    """Checking input for validity"""
    if message.isdigit() and (num := int(message)) > 0:
        return num
    else:
        input_valid_num(input('Enter a natural number: '))


def test_result(verifiable: str, valid: int):
    """Test the result to see if it corresponds to the correct solution"""
    if verifiable in hex(valid):
        print(f'The conversion was successful!')
        print(hex(valid))
    else:
        print(f'Error!')


def main():
    """Programme"""
    user_input = input_valid_num(input('Enter a decimal number: '))
    hex_num = ConvertToHex(user_input)
    convert = hex_num.convert_num(hex_num.get_num())
    print(hex_num)
    test_result(convert, hex_num.get_num())


if __name__ == '__main__':
    main()
