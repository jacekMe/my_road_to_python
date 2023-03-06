## 1 ##

""" Add a class variable names 'square_list' to the 'Square' class, where all
created objects of the 'Square' class will be stored."""

class Square():
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self)

s1 = Square(18)
s2 = Square(8)
s3 = Square(88)
print(Square.square_list)

## 2 ##

""" Change the 'Square' class so that when the 'Square' object is displayed,
a message is presented about the length of all the sides of the square. For 
example, if you create a 'Square(29)' object Python should display the message:
'29 by 29 by 29 by 29'."""

class Square():
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self)

    def __repr__(self):
        return "{} na {} na {} na {} ".format(self.side, self.side, self.side, self.side)

s1 = Square(18)
print(s1)

## 3 ##

""" Write a function that takes two objects as parameters and returns True if
found to be the same object, and False otherwise"""


def similar(x, y):
    return x is y

print(similar(10, 11))
print(similar('a', 'b'))