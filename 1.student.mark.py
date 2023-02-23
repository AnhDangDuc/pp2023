students = []
courses = []
marks = {}
#input functions
def input_students():              
    n_students = int(input("Enter the number of students you want input: "))         #input number of students
    for i in range(n_students):
        student_name = input("Enter the student name: ")
        student_id = input("Enter the student ID: ")
        student_dob = input("Enter the student's DoB: ")
        if student_id in students:                                                   #append if this student isn't on the list
            print("This student is on the list!")
        else:
            students.append((student_id, student_name, student_dob))

def input_courses():                                                                 #append if this course is not on the list
    course_name = input("Enter the course name: ")
    course_id = input("Enter the course id: ")
    if course_id not in courses:
        courses.append((course_name, course_id))
    else:
        print("This course is on the list!")

def input_marks():
    course_id = input("Enter the course ID you what to input marks: ")
    if course_id not in courses:
        for student in students:
            student_id = student[0]
            mark = float(input(f"Enter the mark for this student {student_id}: "))
            if course_id not in marks:
                marks[course_id] = {}
            mark = marks[course_id][student_id]
    else:
        print("We don't learn this course !")

#list functions
def list_students():
    print("student: ")
    for student in students:
        print(f"ID {student[0]} - Name: {student[1]} - DoB: {student[2]}")


def list_course():
    print("Course: ")
    for course in courses:
        print(f"Course name: {course[0]} - Course ID: {course[1]}")


def list_marks():
    course_id = input("Enter the course ID: ")
    if course_id not in marks:
        print("We don't learn this course !")
    else:
        print(f"Marks for course {course_id} is: ")
        for student in students:
            student_id = student[0]
            if student_id in marks[course_id]:
                mark = marks[course_id][student_id]
                print(f"ID: {student[0]} - Mark: {marks}")
            else:
                print("This student is not in this course !")


while(True):
    print("\n0. Exit")
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks")
    print("4. List student infor")
    print("5. List course infor")
    print("6. Show marks for a given course")
    choose = int(input("Enter your choice: "))
    if choose == 0:
        break
    elif choose == 1:
        input_students()
    elif choose == 2:
        input_courses()
    elif choose == 3:
        input_marks()
    elif choose == 4:
        list_students()
    elif choose == 5:
        list_course()
    elif choose == 6:
        list_marks()
    else:
        print("Invalid, please choose one obtion above:")


