# split returns a list
# key in sorted helps give a reference to the function
# lambda is a function without name
# Python supports a CSV library, reader can read lines in a file
# .DictReader which iterates from top to bottom loads each line as a dictonary instead of list but there should be clear markers in the top

import csv

name = input("what's your name? ")
home = input("what's your home? ")

with open("python-core\students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})