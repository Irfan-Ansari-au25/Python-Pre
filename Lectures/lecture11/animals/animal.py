

class Animals:
    def __init__(self, name, no_of_legs, has_tail):
        print("It's a animal constructor.")

        self.name = name
        self.no_of_legs = no_of_legs
        self.has_tail = has_tail


    def eat(self, food):
        print(f"{self.name} is eating {food} !!!")

    def walk(self):
        print(f"{self.name} is walking !!!")



        