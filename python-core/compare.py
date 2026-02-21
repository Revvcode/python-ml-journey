x = int(input("What's x? "))
y = int(input("what's y? "))

# Python supports conditionals like if, else, elif
if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

elif x==y:
    print("x is equal to y")

# logical operators like or exist
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

