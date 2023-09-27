class Student:

def __init__(self, name, roll_number, cgpa} self.name = name

self roll_number = roll_number

self.cgpa capa

def str_(self)

return f"{self.name) (Roll No: (self.roll_number), CGPA: (self.cgpa}}"

def sort students(student_list):

sorted students = sorted (student list, key-lambda student: student.cgpa,

reverse=True)

return sorted students

name

_main_

students = [

Student("Akash", "101", 39),

Student("Dhanush", "102", 3.7), Student("Gowtham Raj", "103", 3.8) Student("Ram", "104", 4.0),

sorted students = sort students(students)

for student in sorted students: print(student)
