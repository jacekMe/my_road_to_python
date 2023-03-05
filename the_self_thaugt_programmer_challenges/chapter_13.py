## 1 ##

""" Define the 'Rectangle' and 'Square' classes the have a 'calculate_perimeter'
method that calculates the perimeter of a given figure. Create 'Rectangle' and 
'Square' objects and the call their 'calculate_perimeter' method. """

class Rectangle():
    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b

    def calculate_perimeter(self):
        return 2 * self.side_a + 2 * self.side_b

class Square():
    def __init__(self, a):
        self.side_a = a

    def calculate_perimeter(self):
        return 4 * self.side_a


rectangle = Rectangle(4, 8)
print(rectangle.calculate_perimeter())

square = Square(8)
print(square.calculate_perimeter())

## 2 ##

""" In the 'Square' class, define the 'change_size' method to increase or 
decrease (if passing a negative value) the lengths of the edges of the square
by the given value. """

class Square():
    def __init__(self, a):
        self.side_a = a

    def calculate_perimeter(self):
        return 4 * self.side_a

    def change_size(self, new_a):
        self.side_a += new_a

square = Square(9)
print(square.side_a)

square.change_size(4)
print(square.side_a)

## 3 ##

""" Create a class 'Square'. Define a 'what_am_i' method in it that will display
the string 'I am a figure'. Modify the 'Square' and 'Rectangle' classes from the
previous challenges so that they inherit from the 'Shape' class. Create 'Square'
and 'Rectangle' objects, then call their 'what_am_i' method."""

class Shape():
    def what_am_i(self):
        print("jestem figurą")

class Rectangle(Shape):
    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b

    def calculate_perimeter(self):
        return 2 * self.side_a + 2 * self.side_b

class Square(Shape):
    def __init__(self, a):
        self.side_a = a

    def calculate_perimeter(self):
        return 4 * self.side_a

a_rectangle = Rectangle(20, 50)
a_square = Square(29)

a_rectangle.what_am_i()
a_square.what_am_i()

## 4 ##

""" Define the class 'Horse' and 'Rider'. Using composition, model the fact that
a horse can have a rider."""

class Horse():
    def __init__(self, name):
        self.name = name

class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

don_horse = Horse("Rosynant")
rider = Rider("Don Kichot", don_horse)
print(rider.horse.name)
