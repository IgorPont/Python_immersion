_journal_dict = {}


def save(question, count):
    _journal_dict[question] = count


def guess(text: str, answer: list[str], count: int) -> int:
    """..."""
    for i in range(count):
        answer_user = input(f'{text}: ').lower()
        if answer_user in answer:
            print('Win!')
            save(text, i + 1)
            return i + 1
    save(text, 0)
    return 0


def journal(dict_, question):
    print('\n'.join(f'Загадка {question} отгадана с {value} попытки' for question, value in _journal_dict.items()))


if __name__ == '__main__':
    res = guess('Зимой и летом одним цветом', ['ель', 'ёлка', 'елка'], 3)
    if res == 0:
        print('False')
    journal()
