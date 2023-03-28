user_input = input('Enter text or number: ')

if user_input.isdigit():
    print(f'{user_input} - a positive integer')
elif user_input.replace('.', '', 1).isdigit():
    print(f'{user_input} - a real positive number')
elif user_input[0] == '-' and user_input[1:].replace('.', '', 1).isdigit():
    print(f'{user_input} - real negative number')
elif user_input.lower() != user_input:
    print(user_input.lower())
elif user_input.upper() != user_input:
    print(user_input.upper())
