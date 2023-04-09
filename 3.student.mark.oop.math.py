import math
import numpy as np

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = []

    def add_marks(self, marks):
        self.marks.append(marks)

    def get_marks(self, course_id):
        for i in range(len(self.marks)):
            if self.marks[i][0] == course_id:
                return self.marks[i][1]

    def __str__(self):
        return "ID: " + str(self.id) + " | Name: " + self.name + " | DoB: " + self.dob

class Course:
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits

    def __str__(self):
        return "ID: " + str(self.id) + " | Name: " + self.name

class MarkSheet:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def get_student(self, student_id):
        for i in range(len(self.students)):
            if self.students[i].id == student_id:
                return self.students[i]

    def get_course(self, course_id):
        for i in range(len(self.courses)):
            if self.courses[i].id == course_id:
                return self.courses[i]

    def get_all_students(self):
        for i in range(len(self.students)):
            print(self.students[i])

    def get_all_courses(self):
        for i in range(len(self.courses)):
            print(self.courses[i])

    def add_marks(self, student_id, course_id, marks):
        marks = math.floor(marks * 10) / 10  # round down to 1 decimal place
        student = self.get_student(student_id)
        student.add_marks((course_id, marks))

    def get_marks(self, student_id, course_id):
        student = self.get_student(student_id)
        return student.get_marks(course_id)

    def calculate_gpa(self, student_id):
        student = self.get_student(student_id)
        total_credits = 0
        total_weighted_points = 0
        for mark in student.marks:
            course = self.get_course(mark[0])
            credits = course.credits
            grade = mark[1]
            total_credits += credits
            total_weighted_points += credits * grade
        return round(total_weighted_points / total_credits, 2)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda x: self.calculate_gpa(x.id), reverse=True)

# sample usage
m = MarkSheet()
while True:
    print("1.Add Student")
    print("2.Add Courses")
    print("3.Add marks")
    print("4.List all student")
    print("5.List all courses")
    print("6.List marks")
    print("7.Calculate GPA for student")
    print("8.Sort students by GPA")
    print("9.Exit")
    choose = int(input("Enter your number: "))
    if choose == 1:
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        student = Student(id, name, dob)
        m.add_student(student)
    elif choose == 2:
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credits = int(input("Enter course credits: "))
        course = Course(id, name, credits)
        m.add_course(course)
    elif choose == 3:
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        marks = float(input("Enter marks: "))
        m.add_marks(student_id, course_id, marks)
    elif choose == 4:
        m.get_all_students()
    elif choose == 5:
        m.get_all_courses()
    elif choose == 6:
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        marks = m.get_marks(student_id, course_id)
        print("Marks:", marks)
    elif choose == 7:
        student_id = input("Enter student ID: ")
        gpa = m.calculate_gpa(student_id)
        print("GPA:", gpa)
    elif choose == 8:
        m.sort_students_by_gpa()
        m.get_all_students()
    elif choose == 9:
        break
    else:
        print("Invalid input")
