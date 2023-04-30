"""
Создайте класс-фабрику.
- Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
- Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.
"""


class Animal:
    def __init__(self, area):
        self.area = area


class Fishes(Animal):
    def __init__(self, area, add_info):
        self.add_info = add_info
        super().__init__(area)

    def __str__(self):
        return f'{type(self).__name__} area = {self.area} info: {self.add_info}'


class Birds(Animal):
    def __init__(self, area, wings):
        self.wings = wings
        super().__init__(area)

    def __str__(self):
        return f'{type(self).__name__} area = {self.area} info: {self.wings}'


class Reptiles(Animal):
    def __init__(self, area, info):
        self.info = info
        super().__init__(area)

    def __str__(self):
        return f'{type(self).__name__} area = {self.area} info: {self.info}'


class AnimalFabric:
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def _get_maker(self, animal_type: str):
        types = {"fishes": Fishes, "birds": Birds, "reptiles": Reptiles}
        return types[animal_type.lower()]


if __name__ == '__main__':
    fabric = AnimalFabric()
    animal_from_fabric = fabric.make_animal("fishes", "glazun", "gold fish")
    animal_from_fabric.commands = ["swim", "eat"]
    print(animal_from_fabric)
