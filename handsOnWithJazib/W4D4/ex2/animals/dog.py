from animal import Animal

class Dog(Animal):
    def __init__(self,name, no_of_legs, has_tail):
        print('Dog constructor is initialized')
        self.name = name
        self.no_of_legs = no_of_legs
        self.has_tail = has_tail

        super(self).__init__(self.name, self.no_of_legs, self.has_tail)

    def bark(self):
        print(self.name, 'is barking.')

    