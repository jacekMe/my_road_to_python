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