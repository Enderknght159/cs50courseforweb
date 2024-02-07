import functions001
print("Welcome to solve equation from type ax^2 + bx + c = 0 so.... Enter a, b and c\n")

while True:
    a = int(input())
    b = int(input())
    c = int(input())
    print(functions001.solvesquare(a, b, c))
