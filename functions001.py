from cmath import sqrt


def solvesquare(a, b, c):
    d = b*b-4*a*c
    if d >= 0:
        x1 = (-b-sqrt(d))/(2*a)
        x2 = (-b+sqrt(d))/(2*a)
    elif d < 0:
        x1 = x2 = None
    sroot = (x1, x2)
    return sroot
