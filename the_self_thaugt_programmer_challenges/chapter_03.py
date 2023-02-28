## Display three different character strings.

print("Hello everyone!")
print("My name is Jacek")
print("Nice to meet you!:)")


## Write a program that prints a message if a variable is less than 10, and a different message is the variable is
## greater than or equal to 10

x = 10

if x < 10:
    print("x is less than 10")
else:
    print("x is greater or equal than 10")


## Wrtie a program that prints a message if a variable is less than or equal to 10, another message is the variable
## is greater than 10 but less than or equal to 25, and another message if the variable is greater than 25

x = 8

if x <= 10:
    print("x is less or equal than 10")
elif x <= 25:
    print("x is greater than 10 but less or equal than 25")
else:
    print("x is greater than 25")


## Create a program that divides to variables and prints the remainder

a = 8
b = 4

c = a % b

print(c)


## Create a program that takes two variables, divides them and prints the quotient

a = 9
b = 4

c = a // b

print(c)


## Write a program with a variable 'age' assigned to an integer that prints different strings depending on what integer
## age is

age = 34

if age < 35:
    print("You're before 35.")
elif age >= 35:
    print("Now it's your time!")
else:
    print("You're alien ;)")


