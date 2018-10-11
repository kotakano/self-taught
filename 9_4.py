import csv

movies = [["トップ・ガン", "リスキービジネス", "マイノリティー・リポート"],["タイタニック", "レヴァナント", "インセプション"],["トレーニング・デイ", "マイ・ボディーガード", "フライト"]]
with open("jp_title.csv", "w", newline='', encoding="cp932") as f:
    w = csv.writer(f, delimiter=",")
    for movie_list in movies:
       w.writerow(movie_list)
