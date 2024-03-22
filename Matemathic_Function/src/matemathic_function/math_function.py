from math import sqrt, pow


class Triangle:

    def area(self):
        pass

    def perimeter(self):
        pass


class EquilateralTriangle(Triangle):

    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return self.side * 3

    def area(self):
        h = sqrt(pow(self.side, 2) - pow(self.side / 2, 2))
        return round(self.side * h * 0.5, 3)


class IsoscelesTriangle(Triangle):

    def __init__(self, base_side, lateral_side):
        self.base_side = base_side
        self.lateral_side = lateral_side

    def perimeter(self):
        return self.lateral_side * 2 + self.base_side

    def area(self):
        h = sqrt(pow(self.lateral_side, 2) - pow(self.base_side / 2, 2))
        return round(self.base_side * h * 0.5, 3)


class ScaleneTriangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        p = self.perimeter() / 2
        return round(sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3)))
    
