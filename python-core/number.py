# try and except can be used to handle exceptional cases
# use this to properly debug, with else we can test cases
# return is like a stronger break
# you can use pass keyword to skip the error message

def main():
    x = get_int("what's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
           pass

main()