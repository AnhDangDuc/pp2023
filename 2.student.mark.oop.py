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
    def __init__(self, id, name):
        self.id = id
        self.name = name

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
        student = self.get_student(student_id)
        student.add_marks((course_id, marks))

    def get_marks(self, student_id, course_id):
        student = self.get_student(student_id)
        return student.get_marks(course_id)

# sample usage
m = MarkSheet()
while True:
    print("1.Add Student")
    print("2.Add Courses")
    print("3.Add marks")
    print("4.List all student")
    print("5.List all courses")
    print("6.List marks")
    print("7.Exit")
    choose = int(input("Enter your number: "))
    if choose == 1:
        # add students
        num_students = int(input("Enter number of students in the class: "))
        for i in range(num_students):
            print(f"\\nStudent {i+1}:")
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (MM/DD/YYYY): ")
            m.add_student(Student(id, name, dob))
    elif choose == 2:
        # add courses
        num_courses = int(input("\\nEnter number of courses: "))
        for i in range(num_courses):
            print(f"\\nCourse {i+1}:")
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            m.add_course(Course(id, name))
    elif choose == 3:
        # add marks
        print("\\nAdd marks for each student in a course:")
        m.get_all_courses()
        course_id = input("Enter the ID of the course you want to input marks for: ")
        m.get_all_students()
        for i in range(num_students):
            print(f"\\nStudent {i+1}:")
            student_id = input("Enter student ID: ")
            marks = float(input(f"Enter marks for student {i+1}: "))
            m.add_marks(student_id, course_id, marks)
    elif choose == 4:
        # list all students
        print("\\nAll students:")
        m.get_all_students()
    elif choose == 5:
        # list all courses
        print("\\nAll courses:")
        m.get_all_courses()
    elif choose == 6:
        # get marks for a given student in a given course
        print("\\nGet marks for a student in a course:")
        m.get_all_students()
        student_id = input("Enter student ID: ")
        m.get_all_courses()
        course_id = input("Enter course ID: ")
        print(f"\\nMarks for student {student_id} in course {course_id}: {m.get_marks(student_id, course_id)}")
    elif choose == 7:
        print("See you again! ")
        break
    else:
        print("Invalid choice, please choose again! ")



