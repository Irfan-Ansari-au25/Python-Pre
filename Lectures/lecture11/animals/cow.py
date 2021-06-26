from animals.animal import Animals

class Cow(Animals):
    def __init__(self, name , no_of_legs, has_tail):
        print("cow is initiated.")
        self.name = name
        self.has_tail = has_tail
        self.no_of_legs = no_of_legs
        super().__init__(self.name, self.no_of_legs, self.has_tail)

    def give_milk(self):
        print (f"{self.name} is giving milk ")


    



