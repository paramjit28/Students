import sqlite3

class create_student:
    def __init__(self):
        self.con = sqlite3.connect('student.db')
        self.cur = self.con.cursor()
    
    def insert_student(self, input_student):
        self.cur.execute(""" INSERT INTO students VALUES(?,?,?,?)""", input_student)
        self.con.commit()

db = create_student()

#db columns
'''First_Name TEXT,
    Last_name TEXT,
    Grade TEXT
    Gender TEXT '''


print('*********************Enter Student Info. *********************')
First_Name = input('First Name: ')
Last_Name = input('Last_Name: ')
Grades = input('Grades: ')
Gender = input('Gender: ')
input_student = (First_Name,Last_Name,Grades,Gender)

db.insert_student(input_student)
print('*********************STUDENT IS ADDED*********************')

