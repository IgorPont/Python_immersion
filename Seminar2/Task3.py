# DEC = 10
#
#
# def convert_to_base(num: int, base: int) -> int:
#     """Convert a decimal number to any base system"""
#     return 0 if num == 0 else convert_to_base(num // base, base) * DEC + num % base
#
#
# print(f'convert num: {convert_to_base(20, 2)}, right res: {bin(11)}')
# print(f'convert num: {convert_to_base(20, 8)}, right res: {oct(111)}')

num = 333333 # число, которое переводим
base = 16 # система исчисления
temp = ''
res = ''
while (num > 0):
    temp += str(num % base)
    num //= base
res = temp[::-1]
print(res)
print(hex(333333))
