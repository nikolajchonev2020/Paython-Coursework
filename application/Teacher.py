from Person import *

class Teacher(Person):
    subject = ""
    year = 0
    salary = 0.00
    def __init__(self, name, address_city, address_street, address_number, age, subject, year, salary):
        self.subject = subject
        self.year = year
        self.salary = salary
        self.name = name
        self.age = age
        self.address = Address(address_city, address_street, address_number)
    def print(self):
        print(self.name+"; Age: "+str(self.age))
        print("Address: "+self.get_address())
        print("Subject: "+self.subject+"; Year: "+str(self.year)+"; Salary: ", end="")
        print(f'{self.salary:.2f}')
    def teach(self):
        print("Teacher teaches: "+self.subject)
        self.salary += 100
        print("New salary: ", end="")
        print(f'{self.salary:.2f}')
    def pay(self, amount):
        print("Teac her pay amount: ", end="")
        print(f'{amount:.2f}')
        self.salary -= amount
        print("New salary: ", end="")
        print(f'{self.salary:.2f}')
