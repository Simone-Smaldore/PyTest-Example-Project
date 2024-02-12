import math


class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):

    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.height == other.height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height * 2) + (self.width * 2)


class Square(Rectangle):

    def __init__(self, side_length) -> None:
        super().__init__(side_length, side_length)
