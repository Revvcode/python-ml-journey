def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
"""
Pythonic expression, exclusive to Python
return True if (n % 2 == 0 ) else return False
"""
def is_even(n):
    return (n % 2 == 0)
    
main()