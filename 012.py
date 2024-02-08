while True:
    try:
        x = int(input("X = "))
        y = int(input("Y = "))
        if y != 0:
            break
        else:
            print("Can't devide by zero")
    except TypeError:
        print("Please enter an intiger")
        continue
    except ValueError:
        print("Please enter an intiger!")
        continue

print(f"{x} Over {y} = {x/y}")


