class Student:

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def getData(self):
        return self.name + self.contact

class ScienceStudent(Student):

    def __init__(self, age):
        self.age = age
        self.name="Test"
        self.contact=" e"


purna = ScienceStudent(20)

print(purna.getData())