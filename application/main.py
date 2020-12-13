from Teacher import *

def heppy_teacher():
    teach.birthday()
    teach.print()

def teacher_teaches():
    teach.teach()

def teacher_print():
    teach.print()

def teacher_pay_amount():
    amn = float(input("How Teacher pay: "))
    teach.pay(amn)

teach = None
teach_name = ""
teach_city = ""
teach_street = ""
teach_number = 0
teach_age = 0
teach_subject = ""
teach_salary = 0.00
while True:
    print("Select:")
    print("1. Create new Teacher")
    print("2. Show Teacher details")
    print("3. Happy Birthday")
    print("4. Techer teches")
    print("5. Teacher pay amount")
    print("0. Exit Program")
    ans = int(input("Enter your choice: "))
    if ans == 0:
        print("Program exit!")
        break
    if ans == 1:
        teach_name = input("Enter Teacher names: ")
        teach_city = input("Enter Teacher City: ")
        teach_street = input("Enter Teacher Street: ")
        teach_number = int(input("Enter Teacher Street Number: "))
        teach_age = int(input("Enter Teacher Ages: "))
        teach_subject = input("Enter Teacher Subject: ")
        teach_salary = float(input("Enter Teacher Salary: "))
        teach = Teacher(teach_name, teach_city, teach_street, teach_number, teach_age, teach_subject, 1, teach_salary)
        continue
    if ans == 2:
        teacher_print()
        continue
    if ans == 3:
        heppy_teacher()
        continue
    if ans == 4:
        teacher_teaches()
        continue
    if ans == 5:
        teacher_pay_amount()
