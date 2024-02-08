games = [
    dict(name="Callof duty", rating=10),
    dict(name="minecraft", rating=9),
    dict(name="geometry dash", rating=6),
    dict(name="game of thrones", rating=5),
    dict(name="batata", rating=1),
]
while True:
    sort1 = int(input("Enter 1 to sort by name or 2 to sort by rating:\n"))
    if sort1 == 1:
        sort = "name"
        break
    elif sort1 == 2:
        sort = "rating"
        break

games.sort(key=lambda game: game[sort])

for GAME in games:
    print(f"Game: {GAME["name"]: <18}Rating: {GAME["rating"]: <}")
