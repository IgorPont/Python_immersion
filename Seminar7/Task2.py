import random
import string


def get_login(count: int, file_name: str) -> None:
    """..."""
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(count):
            length_ = random.randint(4, 7)
            letters = string.ascii_letters
            login_ = ''.join(random.choice(letters) for _ in range(length_)).capitalize()
            for ch in login_:
                if ch in 'aouyei':
                    f.write(f'{login_}\n')


get_login(5, 'test2.txt')


