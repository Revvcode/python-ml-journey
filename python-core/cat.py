#loops are used for repetitive tasks , while, for
#range(n) is a function which starts at n and ends at n-1, NOT at n
#when we use print("something" * n) it prints it n times
#break and continue can be used to exit/repeat loops at will

def main():
    x= get_number()
    meow(x)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
        
    
def meow(n):
    for _ in range(n):
        print("Meow")

main()