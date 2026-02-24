# __name__ is a special variable in python which becomes main when running in cmd line

def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

if __name__ == "__main__" :
    main()