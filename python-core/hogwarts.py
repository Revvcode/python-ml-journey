#Python has lists, similar to array denoted by name_of_list[], the [] param can be empty
#the iterated variable gains the value of the array element
#len function can be used to find length of the list or string
#Dict helps us store key value pairs, denoted by name_of_dict{}, after each key value pair at the end use ","
#for loop in dict shows only KEYS, to access values use name_of_dict[variable], where variable is being iterated
#python supports None keyword which denotes absence of value
students = [
    {"name": "Harry", "house": "Gryffindor" , "patronus": "Stag" },
    {"name": "Hermione", "house": "Gryffindor" , "patronus": "Otter" },
    {"name": "Draco", "house": "Slytherin" , "patronus": None }
]

for student in students:
    print(student["name"], student["house"],student["patronus"], sep=", ")