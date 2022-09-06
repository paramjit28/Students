from dis import pretty_flags
import sqlite3
import json

class Student:

#initalizer for the class
    def __init__(self):
        self.con = sqlite3.connect('student.db')
        self.cur = self.con.cursor()
        self.create_table()

# this is to create the table
    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS students (
            First_Name,Last_Name,Grade,Gender)""")

    
    def search_student(self):
       self.cur.execute(""" SELECT * FROM students """)
       rows = self.cur.fetchall()
       return rows  
    
    def lastname_student(self):
        s = (""" SELECT * FROM students WHERE Last_Name LIKE  """)
        s0 = input("Enter Lname: ")
        s01 = s + "'%" + s0 + "%'"
        self.cur.execute(s01)
        last = self.cur.fetchall()
        return last
    
#if you want to sort by gender

    def gender_student(self):
      search = (""" SELECT * FROM students WHERE Gender IS """)
      search_entry = input("Enter gender to search: ")
      search_input = search + "'" + search_entry + "'"
      self.cur.execute(search_input)
      items = self.cur.fetchall()
      return items
  
db = Student()

#db columns
'''First_Name TEXT,
    Last_name TEXT,
    Grade TEXT
    Gender TEXT '''



print('**** Student Lists by lastname*****')
lname = db.lastname_student()
pretty_data = json.dumps(lname, indent=2)
print(pretty_data)


print('**** Student Lists by Gender*****')
gender = db.gender_student()
pretty_dataGender = json.dumps(gender, indent=2)
print(pretty_dataGender)








    
    

        
  
    
   
