import random

from Task3 import Person


class Worker(Person):
    LEVEL = 7

    def __init__(self, first_name: str, last_name: str, age: int, id: int):
        super().__init__(first_name, last_name, age)
        if 99_999 < id < 1_000_000:
            self._id = id
        else:
            self._id = random.randint(100_000, 999_999)
        self._level = sum(int(num) for num in str(self._id)) % self.LEVEL

    def __str__(self):
        return f'{self.first_name} {self.last_name} id = {self._id} level = {self._level}'


if __name__ == '__main__':
    worker_1 = Worker('Igor', 'Pont', 37, 987654)
    print(worker_1)
