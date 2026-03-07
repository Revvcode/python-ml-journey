#you can return a list or dictionary based on need
#classes help you define a blueprint to create objects, class is bascially a custom data type
#raise helps make our own errors
#classes help make it easier for users to skip repeated code blocks in general too
import re
class Student:
    def __init__(self,name,house):
        if not name: # literally if name == ""
            raise ValueError("Missing name")
        if (house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]):
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name,house)


if __name__ == "__main__":
    main()