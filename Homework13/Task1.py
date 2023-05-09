"""
Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях. Напишите к ним
классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например,
нельзя создавать прямоугольник со сторонами
отрицательной длины.
"""


class Rectangle:
    def __init__(self, width: int | float, height: int | float | None = None):
        if width <= 0:
            raise NegativeSizeError(width)
        elif height <= 0:
            raise NegativeSizeError(height)
        self._width = width
        self._heigth = height or width

    def perimeter(self) -> float:
        return 2 * (self._width + self._heigth)

    def area(self) -> float:
        return self._width * self._heigth

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('Not a "Rectangle" instance')
        ratio_width = self._width / self.perimeter()
        retio_height = self._heigth / self.perimeter()
        new_perimetr = self.perimeter() + other.perimeter()
        return Rectangle(new_perimetr * ratio_width, new_perimetr * retio_height)

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('Not a "Rectangle" instance')
        ratio_width = self._width / self.perimeter()
        retio_height = self._heigth / self.perimeter()
        new_perimetr = abs(self.perimeter() - other.perimeter())
        return Rectangle(new_perimetr * ratio_width, new_perimetr * retio_height)

    def __eq__(self, other):
        """равны ли по площади"""
        return self.area() is other.area()

    def __ne__(self, other):
        """не равны ли по площади"""
        return self.area() is not other.area()

    def __gt__(self, other):
        """больше ли по площади"""
        return self.area() > other.area()

    def __lt__(self, other):
        """меньше ли по площади"""
        return self.area() < other.area()

    def __str__(self):
        return (f'\nRectangle:\n{self._width} x {self._heigth}'
                f'\nPerimetr: {self.perimeter()}'
                f'\nArea:     {self.area()}')

    def __repr__(self):
        return f'Rectangle({self._width}, {self._heigth})'


class UserException(Exception):
    pass


class NegativeSizeError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'The length or width ({self.value}) of the rectangle cannot be negative'


if __name__ == '__main__':
    rectangle_1 = Rectangle(10, 20)
    rectangle_2 = Rectangle(14, 7)
    rectangle_3 = rectangle_1 + rectangle_2
    print(rectangle_3)
