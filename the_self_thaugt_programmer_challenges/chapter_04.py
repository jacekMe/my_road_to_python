## 1. Write a function that takes a number as an input and returns that number 
## square

x = int(input("Give the number: "))
def square_result(x):
    """
    returns x * x.
    :param x: int
    """
    return x ** 2

print(square_result(x))

## 2. Create a function that accepts a string as a parameter and prints it

s = input("Write a sentence: ")

def print_string(s):
    """
    prints a string.
    :param: str
    """
    print(s)

print(print_string(s))


## 3. Write a function that takes three required parameters and two optional 
## parameters

def numbers(a, b, c, x = 8, y = 18):
    """
    adds three numbers together and prints the sum. Values 18, and 8 are
    substituted if no values are passed.
    :param a: int
    :param b: int
    :param c: int
    :param x: int lub 8
    :param y: int lub 18
    :return: suma a, b, c
    """
    return a + b + c

print(numbers(8))


## 4. Write a program with two functions. The first function should take an 
## integer as a parameter and return the result of the integer divided by 2.
## The second function should take an integer as a parameter and return the 
## result of the integer multiplied by 4. Call the first function, save the 
## result as a variable, and pass it as a parameter to the second function.

def divide_by_two(x):
    """
    takes a value and divides it by two.
    :param x: int
    :return: z
    """
    global z
    z = x / 2
    return z

def multiply_by_four(z):
    """
    takes a variable from function 'divide_by_two' and multiply it by four
    :param z: int
    :return: z * 4
    """
    return z * 4

print(divide_2(2))
print(multiply_4(z))


## 5. Write a function that converts a string to a float and returns the result.
## Use exception handling to catch the exception that would occur.

def conv_float(x):
    """
    converts a string to a value of type 'float'
    :param x: str
    :return: float
    """
    try:
        return float(x)
    except(ValueError):
        print("str cannot be converted to float")

print(conv_float("hello"))
print(conv_float("100.10"))
