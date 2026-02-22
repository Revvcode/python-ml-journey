def hello(to="world"):
    print("hello,",to)

#Strings have title() and strip() functions for ease of use
# In print function you can use sep="" and end="" to make changes to how it actually prints
hello()
name = input("what's your name? ")
hello(name)