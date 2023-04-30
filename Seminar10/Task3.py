class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age

    def birthday_up(self):
        self._age += 1

    def get_age(self):
        return self._age

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


if __name__ == '__main__':
    person_1 = Person('Igor', 'Pont', 36)
    print(person_1, person_1.get_age())
    person_1.birthday_up()
    print(person_1, person_1.get_age())
