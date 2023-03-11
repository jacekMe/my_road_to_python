# EXERCISE 1.1
""" Write a program that calculates the area of a rectangle. The values of the sides 'a' and 'b' are of type float
and should be entered from the keyobard. Display the result of the programme on the computer screen."""

# print("The programme calculates the area of a rectangle")
#
# a = float(input("Give the number for side 'a': "))
# b = float(input("Give the number for side 'b': "))
#
# print()
#
# area = a * b
#
# print(f"For 'a' = {a} and 'b' = {b}")
# print(f"The area of a rectangle = {area}")
#

## EXERCISE 1.2
""" Write a program that dispalys the value of a predefined constant on the computer screen 'pi = 3.14...'. Adopt a 
format for displaying this constant to three decimal places."""
#
# import math
#
# print("The programme displays the constant pi with a given accuracy.")
# print("pi = %5.3f"% math.pi, ".", sep="")


## EXERCISE 1.3
""" Write a program that displays on a computer screen the square root of a square root from the predefined value 
'pi = 3.14' to four decimal places after the decimal point."""

# import math
#
# print("""The program displays the square root of 'pi' to four decimal places after the decimal point""")
# print(f"sqrt(pi) = {math.sqrt(math.pi):.4f}", ".", sep="")


## EXERCISE 1.4
""" Write a program that calculates the result of integer division without remainder for two integers 'a=37' 
and 'b=11' """
#
# a = 37
# b = 11
#
# print("The program displays the result of integer division without remainder for two integers 'a' and 'b'.")
# print("For numbers: a = %2i and b = %2i" % (a,b))
# print("%2i // %2i = " % (a,b), a // b, ".", sep="")


## EXERCISE 1.5
""" Write a program that calculates the remainder from integer division of two integers 'a = 37' and 'b = 11'. """

# a = 37
# b = 11
#
# print("The program calculates the remainder from integer divison of two integers 'a' and 'b'.")
# print(f"For numbers: a = {a} and {b}")
# print(f"{a} % {b} = {a % b}", ".", sep="")


## EXERCISE 1.6
""" Write a program that reads in the first name, last name, age and price of bread, and then prints these four 
variable on the computer screen."""
#
# first_name = input("Give your first name: ")
# last_name = input("Give your last name: ")
# age = int(input("How old are you? "))
# price = float(input("How much did you pay for bread? "))
#
# print()
#
# print("Here is the data you have entered: ")
# print("First name: ", first_name, ".", sep="")
# print("Last name: ", last_name, ".", sep="")
# print("Age: ", age, "years old.")
# print("Bread cost: ", price, "zł.")



## exercise 1.7
""" Write a program that generates 5 pseudorandom numbers from the interval 1 to 100."""

import random

print("Pseudorandom numbers: ")
print()

for i in range(5):
    number = random.randint(1, 100)
    print(number)
