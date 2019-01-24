import math as m


class Shape:
    # constructor
    def __init__(self, dimensions):
        self.dimension = list(dimensions)
        self.name = self.get_name()
        self.area = self.get_area()

    def get_name(self):
        if len(self.dimension) == 4:
            if len(set(self.dimension)) == 1:
                return "square"
            if len(set(self.dimension)) == 2:
                return "rectangle"
            else:
                return "unrecognised"
        elif len(self.dimension) == 3:
            return "triangle"

    def get_area(self):
        if self.name == "rectangle":
            area = 1
            for side in set(self.dimension):
                area *= side
            return area
        elif self.name == "square":
            area = (self.dimension[0]) * (self.dimension[0])
            return area
        elif self.name == "triangle":
            a = self.dimension[0]
            b = self.dimension[1]
            c = self.dimension[2]
            s = (a + b + c) / 2
            # using heron's formula for calculating area of triangle
            try:
                area = m.sqrt(s * (s - a) * (s - b) * (s - c))
            except:
                area = "undefined"
            return area
        else:
            return "undefined"


if __name__ == '__main__':
    dimensions = (input("Enter measurements of all sides of the shape : ")).split(" ")
    dimensions = map(float, dimensions)

    shape = Shape(dimensions)
    print("The shape is a ", shape.name, " shape with an area of ", shape.area)
