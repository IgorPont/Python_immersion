import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_length(self):
        return math.pi * self.radius * 2

    def circle_square(self):
        return math.pi * (self.radius ** 2)


if __name__ == '__main__':
    circle_1 = Circle(5)
    print(circle_1.circle_length())
    print(circle_1.circle_square())
