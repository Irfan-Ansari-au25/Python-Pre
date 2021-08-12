from student import Student

if __name__ == '__main__':
    name = input('Enter the name of the student')
    age = int(input('Enter the age of the student'))
    birth = int(input('Enter the birth date of the student'))
    pradeep = Student(name,age,birth)
    print(pradeep.name)
    print(pradeep.age)
    pradeep.read()