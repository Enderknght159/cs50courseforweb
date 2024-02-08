# decorators:
def announce(f):
    def wrapper():
        print(f"Running ...")
        f()
    return wrapper


@announce
def hello():
    print("Hello World!")


hello()