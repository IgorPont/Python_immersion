class Rectangle:
    def __init__(self, width: int | float, height: int | float | None = None):
        self._width = width
        self._heigth = height or width

    def perimeter(self) -> float:
        return 2 * (self._width + self._heigth)

    def area(self) -> float:
        return self._width * self._heigth


if __name__ == '__main__':
    rectangle_1 = Rectangle(5)
    print(rectangle_1.perimeter())
    print(rectangle_1.area())
