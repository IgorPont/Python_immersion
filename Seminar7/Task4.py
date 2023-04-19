import random
import string


def file_generator(expansion: str, min_length_name: int = 6, max_length_name: int = 30,
                   min_number_byte: int = 256, max_number_byte: int = 4096, file_count: int = 42) -> None:
    for i in range(file_count):
        string_name = ''
        random_length = random.randint(min_length_name, max_length_name)
        for j in range(random_length):
            string_name += random.choice(string.ascii_letters)

        random_byte = random.randint(min_number_byte, max_number_byte)
        data = bytes(random_byte)
        with open(f'{string_name}.{expansion}', 'ab') as f:
            f.write(data)


if __name__ == '__main__':
    file_generator('txt', file_count=1)
