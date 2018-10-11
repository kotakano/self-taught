import csv

movies = [["Top Gun", "Risky Business", "Minority Report"],["Titanic", "The Revenant", "Inception"],["Training Day", "Man on Fire", "Flight"]]
with open("title.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for movie_list in movies:
       w.writerow(movie_list)

