def get_number(user_input: str) -> int | float:
    while True:
        num = input(user_input)
        try:
            return int(num)
        except ValueError as e:
            try:
                return float(num)
            except ValueError as e:
                print(f'You entered the wrong number: {e}')


if __name__ == '__main__':
    print(get_number('Enter an integer or a real number: '))
