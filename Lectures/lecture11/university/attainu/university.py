

class University:
    def __init__(self, name, no_of_students,  batches):
        self.name = name
        self.no_of_students = no_of_students
        self.batches = []

        print("University constructor initialized")


    def add_batches(self, batch):
        self.batches.append(batch)

    

    def print_batches(self):
        for batch in self.batches:
            print(batch.batch_name, batch.name, batch.no_of_students)