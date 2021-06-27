from attainu.university import University
from attainu.batch import Batch

if __name__ == '__main__':

    aec = University("AEC", 100, 3)

    attainu = Batch("Subramanayam", 20 , "aec", 40, "gold")

    attainu.add_batches(attainu)
    attainu.print_batches()