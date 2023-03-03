## 1. Find for your computer some file and print it content.

with open("""/home/jacekmeres/programming/courses/sql/course_nieinformatyk
    /01_zalety_bazy_danych.txt""", 'r') as f:
    print(f.read())


## 2. Write a program which make user question and save answer in file.

clubs = input('What do you know club from Premier League?: ')

with open('premier_league_clubs.txt', 'w') as f:
    f.write(clubs)


## 3. Write a program which save in file CSV content of list which consists of
## few lists. Data each of list should save in separate row and separated by
## commas.

movies = [["Top Gun", "Ocean's Eleven", "Minority Report"], 
        ["Titanic", "The Last Jedi", "Inception"],
        ["Pulp Fiction", "Django", "Once Upon a Time... in Hollywood"]]

with open("movies.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=',')
    for movie in movies:
        write.writerow(movie)