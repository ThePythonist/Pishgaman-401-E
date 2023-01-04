class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname


class Student(Person):
    def __init__(self, fname, lname, id):
        super().__init__(fname, lname)
        self.id = id


y = Person("Mike", "Olsen")
x = Student("Mike", "Olsen", 124256)
print(x.firstname)
