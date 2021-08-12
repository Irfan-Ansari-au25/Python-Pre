class Student:
    # Constructor
    def __init__(self,n,a,b):
        """
        name denotes name of the student
        age denotes age of the student
        birth_year denotes birth_year of the student
        """
        self.name = n
        self.age = a
        self.birth_year = b

    def read(self):
        print('Student', self.name,
            'is reading')

    def write(self):
        print(f'student {self.name} is writing.')


