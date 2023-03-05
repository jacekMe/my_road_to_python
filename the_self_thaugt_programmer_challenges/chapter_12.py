## 1 ##

""" Define an 'Apple' class with four instance variables representing four
different characteristics of apples."""

class Apple():
    def __init__(self, w, c, t, s):
        self.weight = w
        self.color = c
        self.type = t
        self.size = s

        print("Done!")

apple = Apple(120, 'green', 'jonagold', 'medium')
print(apple)
print(apple.weight)
print(apple.color)
print(apple.type)
print(apple.size)


## 2 ##

""" Define the 'Circle' class with an 'area' method that calculates and returns
the area of a circle. Then create a 'Circle' object, call its 'area' method
and display the result. Use the 'pi' function available in the 'math'
built-in module. """

import math

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi

circle = Circle(4)
print(circle.area())


## 3 ##

""" Define a 'Triangle' calss with an 'area' method that calculates and returns
the area of a triangle. Then create a 'Triangle' object, call its 'area' method
and display the result. """

class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.base * self.height / 2

triangle = Triangle(6, 4)
print(triangle.area())


## 4 ##

""" Define a class 'Hexagon' having a method called 'calculate_perimeter' that
calculates and returns the perimeter of a hexagon. Then create an object of this
class, call its 'calculate_perimeter' method and display the result reutrned 
by it. """

class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6


    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6

hexagon = Hexagon(2, 5, 8, 1, 4, 9)
print(hexagon.calculate_perimeter())