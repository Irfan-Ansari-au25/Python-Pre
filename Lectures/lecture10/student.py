"""
class file name should me in lowercase
class name should be in uppercase

constructor function execute when object or instance is created
there are attrubutes and methods in a class

"""

class Student:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    

    def calc_age(self):
        print(f"{self.name} is {2021 -  self.birth_year} years old")

    def read(self, book):
        print(f"{self.name} is reading a {book} book!!!")