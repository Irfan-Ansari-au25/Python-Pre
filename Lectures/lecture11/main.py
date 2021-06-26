from animals.animal import Animals
from animals.cow import Cow



if __name__ == '__main__':
    dog = Animals("Rheo", 4, True)
    dog.eat("Grass")
    dog.walk()

    cow = Cow("mea", 4, True)
    cow.eat("chicken")
    cow.give_milk()