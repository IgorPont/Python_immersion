class IsPositive:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f'Стороны прямоугольника должны быть положительными')
        setattr(instance, self.param_name, value)


class Foursquare:
    # __slots__ = ('_a', '_b')
    _a = IsPositive()
    _b = IsPositive()

    def __init__(self, a, b=0):
        self._a = a
        if b == 0:
            self._b = a
        else:
            self._b = b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError(f'The length must be greater than zero')

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise ValueError(f'The width must be greater than zero')

    def perimeter(self) -> float:
        return 2 * (self._a + self._b)

    def area(self) -> float:
        return self._a * self._b


if __name__ == '__main__':
    foursquare_1 = Foursquare(-5, 10)
    print(foursquare_1.area())
    foursquare_1.a = 7
    foursquare_1.b = 15
    print(foursquare_1.area())
    # print(Foursquare.__dict__)
    # print(foursquare_1.__dict__)
