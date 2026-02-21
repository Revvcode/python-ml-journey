name = input("What's your name? ")

# Match keyword - similar to switch() from C and no need for default, use _
match name:
    case "Jagan" | "Wadina":
        print("Red")
    
    case "Amira":
        print("Blue")

    case _:
        print("Green")