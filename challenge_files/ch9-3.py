import csv

movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fine", "Flight"]]
with open ('movies.csv', "w", newline='') as f:
    spawnwriter = csv.writer(f, delimiter=",")
    for movie_list in movies:
        spawnwriter.writerow(movie_list)
