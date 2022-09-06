import sqlite3

class delete_Student:

    def __init__(self):
        self.con = sqlite3.connect('student.db')
        self.cur = self.con.cursor()

    
    def delete_student(self):
       self.cur.execute(""" DELETE FROM students WHERE Last_Name LIKE '' """)
       self.con.commit()
    
db= delete_Student()

db.delete_student()
print('***Blank list is deleted***')




