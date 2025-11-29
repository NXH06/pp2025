# functions
def input_students():
    student_amt = int(input("Input amount of students: "))
    students = []
    for i in range (student_amt):
        student_id = input(f"Input ID of student {i}: ")
        student_name = input(f"Input name of student {i}: ")
        student_dob = input(f"Input date of birth (YYYY-MM-dd) of student {i}: ")
        students.append(s_dict(student_id, student_name, student_dob))
    return students
def input_courses():
    course_amt = int(input("Input amount of courses: "))
    courses = []
    for i in range (course_amt):
        course_id = input(f"Input ID of course {i}: ")
        course_name = input(f"Input name of course {i}: ")
        courses.append(c_dict(course_id, course_name))
    return courses
def input_marks():
    global students, courses
    marks = []
    cont = "y"
    while cont == "y":
        s_id = input("Input student ID to give marks for: ")
        c_id = input("Input course ID to give marks for: ")
        mark = float(input(f"Input mark: "))
        marks.append(m_dict(s_id, c_id, mark))
        cont = input("Continue inputting marks? (y/n): ")
    return marks
def list_students():
    for i in range (len(students)):
        print(students[i])
def list_courses():
    for i in range (len(courses)):
        print(courses[i])
def list_marks():
    for i in range (len(marks)):
        print(marks[i])
# some functions for quick sample input (for code testing purposes)
def s_dict(id, name, dob):
    return {"id": id, "name": name, "dob": dob}
def c_dict(id, name):
    return {"id": id, "name": name}
def m_dict(s_id, c_id, mark):
    return {"student_id": s_id, "course_id": c_id, "mark": mark}
def testinput():
    global students, courses, marks
    students = [s_dict("123", "Hien", "2006-02-24"), s_dict("456", "Khoa", "1980-05-11")]
    courses = [c_dict("m1", "math"), c_dict("p2", "physics"), c_dict("i3", "informatics")]
    marks = [m_dict("123", "m1", "15"), m_dict("123", "p2", "16"), m_dict("456", "p2", "18")]
# main code
students = input_students()
courses = input_courses()
marks = input_marks()
print("Listing students... ")
list_students()
print("Listing courses... ")
list_courses()
print("Listing marks...")
list_marks()
