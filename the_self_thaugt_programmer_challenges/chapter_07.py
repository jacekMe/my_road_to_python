## 1. Print each item in the following list: ["The Walking Dead", "Entourage", 
## "The Sopranoa", "The Vampire Diaries"]

movies = ["The Walking Dead", "Entourage", "The Sopranoa", "The Vampire Diaries"]

for show in movies:
    print(show)


## 2. Print all the numbers from 25 to 50.

for i in range(25, 51):
    print(i)


## 3. Print each item from the first challenge and their indexes

movies = ["The Walking Dead", "Entourage", "The Sopranoa", "The Vampire Diaries"]

for i, m in enumerate(movies):
    print(i, m)


## 4. Write a program with an infinite loop (with the option to type 'q' to quit)
## and a list of numbers. Each time through the loop ask the user to guess a 
## number on the list and tell them whether or not they guessed correctly

numbers = [18, 8, 27, 88, 42, 69, 99, 33]

while True:
    x = int(input("Guess a number: "))
    if x in numbers:
        print("Great guess!")
    else:
        print("That's wrong!")
    c = input("Are we continuing to play? (enter 'q' to quit): ")
    if c == 'q':
        break


## 5. Multiply all the numbers in the list [8, 19, 148, 4] with all the numbers 
## in the list [9, 1, 33, 83] and append each result to a third list.

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]

multiply = []

for i in list1:
    for j in list2:
        multiply.append(i * j)

print(multiply)

