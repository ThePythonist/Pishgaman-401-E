from math import pi


class Shape:
    def __init__(self, l=0, w=0, r=0):
        self.length = l
        self.width = w
        self.radius = r

    def rec_area(self):
        print(self.length * self.width)

    def rec_perimeter(self):
        print((self.length + self.width) * 2)

    def circle_area(self):
        print((self.radius ** 2) * pi)

    def circle_perimeter(self):
        print(self.radius * 2 * pi)


while True:
    shape = input("Enter shape : ").casefold()
    if shape == "rectangle":
        l = int(input("Enter length : "))
        w = int(input("Enter width : "))

        rectangle = Shape(l=l, w=w)
        rectangle.rec_area()
        rectangle.rec_perimeter()
        break

    elif shape == "circle":
        r = int(input("Enter radius : "))

        circle = Shape(r=r)
        circle.circle_area()
        circle.circle_perimeter()
        break
    else:
        print("Invalid input")
