for i in range(1, 101):
    if i % 15 == 0:
        i = 'FizzBuzz'
    elif i % 3 == 0:
        i = 'Buzz'
    elif i % 5 == 0:
        i = 'Fizz'
    print(i)

gen = ('FizzBuzz' if i % 15 == 0 else 'Buzz' if i % 3 == 0 else 'Fizz' if i % 5 == 0 else i for i in range(1, 101))
print(*gen)
