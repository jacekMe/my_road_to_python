## EXERCISE 2.1
""" Write a program that, for three numbers 'a', 'b' and 'c' entered from the keyboard checks whether they are
 Pythagorean triples. In addition, assume that a > 0, b > 0 and c > 0."""

print("The programme checks whether numbers a, b, and c they are Pythagorean triples.")

a = int(input("Give the number a: "))
b = int(input("Give the number b: "))
c = int(input("Give the number c: "))

if a * a + b * b == c * c:
    print("Numbers a = ", a, ", b = ", b, " and c = ", c, " form a Pythagorean triples.", sep= "")
else:
    print("Numbers a = ", a, ", b = ", b, " and c = ", c, " not form a Pythagorean triples.", sep= "")


## EXERCISE 2.2
""" Write a program that calculates the value of 'x' from the equation 'ax + b = c'. The values of 'a', 'b' and 'c'
 belong to the set of real numbers and are entered from the keyboard. In addition, protect the programm in case the
 entered value of a is equal to zero. For the variables 'a', 'b' and 'c' and 'x', the format should be adopted to 
 display them to two decimal places."""

print("The programme calculates the value of 'x' from the linear equation 'ax + b = c.")

a = float(input("Give the number a.\n"))

if a == 0:
    print("Unacceptable coefficient value.")
else:
    b = float(input("Give the number b.\n"))
    c = float(input("Give the number c.\n"))

    x = (c - b) / a

    print("For a = ", a, ", b = ", b, " and c = ", c, " value x = ", x, ".", sep= "")


## EXERCISE 2.3
""" Write a program that calculates the roots of a quadratic equation ax² + bx + c = 0, where the variables a, b, c are
real numbers entered from the keyboard. For the variables a, b, c, x1 and x2 adopt the format of displaying them on the
screen to two decimal places."""

import math

print("The programme calculates the roots of a quadratic equation for any coefficients a, b, c.")

a = float(input("Give a number for 'a'.\n"))

if a == 0:
    print("Inadmissible value of the coefficient 'a'. Programme exit.")
    exit()
else:
    b = float(input("Give a number for 'b'.\n"))
    c = float(input("Give a number for 'c'.\n"))

    print("For entered number: ", end ="")
    print("a = ", a, ", b = ", b, " and c = ", c, sep="")

    delta = b * b - 4 * a * c

    if delta < 0:
        print("No real elements.")
    elif delta == 0:
        x1 = - b / (2 * a)
        print("A triangle has one double element x1 = ", x1, ".", sep="")
    else:
        x1 = (- b - math.sqrt(delta))/(2 * a)
        x2 = (- b + math.sqrt(delta))/(2 * a)

        print("A triangle has two elements:")
        print("x1 = ", x1, ",", sep="")
        print("x2 = ", x2, ",", sep="")


## EXERCISE 2.4
""" Write a program that illustrates the operation of the logical operator 'or'."""

a = True
b = True

print("The programme illustrates the operation of the logical operator 'or'.")
print("True or True -> ", a or b, ".", sep="")
print("False or True -> ", not a or b, ".", sep="")
print("True or False -> ", a or not b, ".", sep="")
print("False or False -> ", not a or not b, ".", sep="")


## EXERCISE 2.5
""" Write a program that illustrates the operation of the logical operator 'and'."""

a = True
b = True

print("The programme illustrates the operation of the logical operator 'and'.")
print("True and True -> ", a and b, ".", sep="")
print("False and True -> ", not a and b, ".", sep="")
print("True and False -> ", a and not b, ".", sep="")
print("False and False -> ", not a and not b, ".", sep="")


## EXERCISE 2.6
""" Using the operators 'or', 'and' and 'not, write a program that checks de Morgan's first law."""

a = True
b = True

left_side = not (a and b)
right_side = (not a) or (not b)

if left_side == right_side:
    print("de Morgran's first law is OK")
else:
    print("WOW! Have you discovered a new law?")


## EXERCISE 2.7
""" The following piece of programme code:
a = 5
b = 5

operation = 'adding'

if operation == 'adding':
    score = a + b
else:
    score = a - b

print(result)
rewrite using a three-argument conditional statement."""

a = 18
b = 18

operation = "adding"

score = a + b if operation == "adding" else a - b
print("Score = ", score, ".", sep="")


## EXERCISE 2.8
""" Write a program which, using the 'if-else' construction, compares wiht each other two names: Mirek and Marek."""

name1 = "Mirek"
name2 = "Marek"

if name1 == name2:
    print("The names are the same.")
else:
    print("The names", name1, "and", name2, "are different.")


## EXERCISE 2.9
""" Write a programme that, using the 'if-else' consturction verifies the password entered."""

psswd = input("Enter password: ")

if psswd == "abcd":
    print("Password: ", psswd, " is correctly.", sep="")
else:
    print("Password ", psswd, " is not correctly.", sep="")
