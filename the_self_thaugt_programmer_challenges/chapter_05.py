## 1. Create a list of your favorite musicians

favourite_musician = ["Dawid Podsiadło", "Taco Hemingway", "Jay-Z", "Dr. Dre", 
                    "Coldplay"]

print(favourite_musician)


## 2. Create a list of tuples, with each tuple containing the longitude and
## latitude of somewhere you've lived or visited

places = [(50.48253, 17.33105), (51.93560, 15.50677),
(54.35142, 18.64114), (52.2297700, 21.0117800)]

print(places)


## 3. Create a dictionary that contains different attributes about you:
## height, favorite color, favorite author, etc.

about_me = {
        "height": 178,
        "favorite color": "blue",
        "favorite author": "Walter Isaacson",
        "favorite movie": "Pulp Fiction",
        "favorite football club": "Liverpool FC",
        "sports": ["cycling", "jogging", "swimming", "football"]
        }

print(about_me)


## 4. Write a program that lets the user ask your height, favorite color, or
## favorite author and returns the result from the dictionary you created
## in the previous challenge

want_to_know = input("""What would you like to know? Please enter height, color, 
    author,food or movie: """)

if want_to_know in about_me:
    show_info = about_me[want_to_know]
    print(show_info)
else:
    print("Information not available.")

## 5. Create a dictionary maping your favorite musicians to a list of your 
## favorite songs by them

fav_musicians_and_songs = {
    "Dawid Podsiadło": ["mori", "awejniak", "Kosmiczne Energie", 
                        "Where Did Your Love Go?"],
    "Taco Hemingway": ["Karimata", "6 zer", "Wszystko Jedno", "Trójkąt", ],
    "Jay-Z": ["Empire Stat of Mind", "Numb/Encore", "Ni**as In Paris" ],
    "Dr. Dre": ["Still D.R.E", "The Next Episode", ]
    "Coldplay": ["Viva La Vida", "My Universe", "Something Just Like This",
                "Yellow"]
    }

## 6. What are sets in Python?
""" Set is one of 4 built-in data types in Python used to store collections 
of data. 
Set type has the following characteristics:
- unordered
- elements are unique
- duplicate elements are not allowed
- a set utself may be modified, but the elements contained in the set must
be of an immutable type
"""