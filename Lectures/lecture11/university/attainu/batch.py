from attainu.university import University

class Batch(University):
    def __init__(self, batch_name, strength, name, no_of_students, batches):
        self.batch_name = batch_name
        self.strength = strength
        self.name = name
        self.no_of_students = no_of_students
        self.batches = batches

        super().__init__(self.name, self.no_of_students, self.batches)

        print("University constructor is initialized from batch class.")
