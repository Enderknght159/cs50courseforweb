# lamnbda
shows = [
    dict(name="Attack on titan", rating=10),
    dict(name="Deathnote", rating=9),
    dict(name="Stiens Gate", rating=9),
    dict(name="Demon Slayer", rating=7),
    dict(name="Made In Abyss", rating=9),
    dict(name="One Piece", rating=5),
]

while True:
    x = int(input("Enter 1 to sort by name\nEnter 2 to sort by rating\n"))
    if x == 1:
        sort = "name"
        break
    elif x == 2:
        sort = "rating"
        break
    else:
        print("Please Follow the instructions:")

# instead of:
# def f(n):
#     return n[sort]

# we use lambda
shows.sort(key=lambda n: n[sort])
for show in shows:
    print(f"Show: {show["name"]: <15}Rating: {show["rating"]: <15}")
