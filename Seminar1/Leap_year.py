year = int(input('Введите год, который ходтите проверить на високосный'))
GREGORIAN = 1584
if year < GREGORIAN:
    output_str = 'The year you entered does not belong to the Gregorian calendar'
elif year % 400 == 0:
    output_str = 'Leap year'
elif year % 100 == 0:
    output_str = 'Ordinary year'
elif year % 4 == 0:
    output_str = 'Leap year'
else:
    output_str = 'Ordinary year'
print(output_str)

# Остановился на 1:35