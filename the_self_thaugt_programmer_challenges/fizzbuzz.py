""" Write a program to display numbers from 1 to 100. For multiples of 3, the 
program should display 'Fizz' instead of the number, and for multiples of 5, it
should display 'Buzz'. For numbers that are multiples of both 3 and 5, the 
program should dispaly 'FizzBuzz' instead of the number."""

def fizz_buzz():
    list_fb = [1, 2, 3]
    for i in list_fb:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz()
list_fb = [1, 2, 3]
print(type(list_fb))
list_fb = list(range(1, 4))
print(list_fb)
print(type(list_fb))