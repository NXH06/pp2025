# functions
def input_students():
    global students
    student_amt = int(input("Input amount of students: "))
    for i in range (student_amt):
        student_id = input(f"Input ID of student {i + 1}: ") # Avoid zero-indexing while printing
        student_name = input(f"Input name of student {i + 1}: ")
        student_dob = input(f"Input date of birth (YYYY-MM-dd) of student {i + 1}: ")
        students.append(s_dict(student_id, student_name, student_dob))
def input_courses():
    global courses
    course_amt = int(input("Input amount of courses: "))
    for i in range (course_amt):
        course_id = input(f"Input ID of course {i + 1}: ")
        course_name = input(f"Input name of course {i + 1}: ")
        courses.append(c_dict(course_id, course_name))
def init_marks(): # make 2D table of marks, all filled with placeholder values
    global marks
    for s in students:
        s_id = s["id"]
        marks[s_id] = {}
        for c in courses:
            c_id = c["id"]
            m_dict(s_id, c_id, "x") # placeholder value if the student doesn't have any marks in that course
    return marks
def input_marks():
    global marks
    if students == [] or courses == []:
        print("Input students and courses before inputting marks!")
        return
    if marks == {}:
        marks = init_marks()
    c_id = input("Input course ID to give marks: ")
    s_id = input("Input student ID to give marks: ")
    mark = float(input("Input mark: "))
    m_dict(s_id, c_id, mark)
def list_students():
    if students == []:
        print("Students list is currently empty.")
        return
    print("> Listing students... ")
    for i in range (len(students)):
        print(students[i]) # the print command automatically inserts newline at end
def list_courses():
    if courses == []:
        print("Courses list is currently empty.")
        return
    print("> Listing courses... ")
    for i in range (len(courses)):
        print(courses[i])
def list_marks():
    if marks == {}:
        print("Marks list is currently empty.")
        return
    print("> Listing marks...")
    for student in marks:
        print(f"{student}: {marks[student]}")
# Functions for speeding up work with dictionaries
def s_dict(id, name, dob):
    return {"id": id, "name": name, "dob": dob}
def c_dict(id, name):
    return {"id": id, "name": name}
def m_dict(s_id, c_id, mark):
    global marks
    marks[s_id][c_id] = mark
# Function for a quick sample input (for code testing purposes). Working with command-line only is too slow...
def testinput():
    global students, courses, marks
    if students != [] or courses != []:
        print("Cannot use sample input since there is already data in [students] or [courses].")
        return
    print("> Creating sample input...")
    students = [s_dict("123", "Hien", "2006-02-24"), s_dict("456", "Khoa", "1980-05-11")]
    courses = [c_dict("m1", "math"), c_dict("p2", "physics"), c_dict("i3", "informatics")]
    marks = init_marks()
    m_dict("123", "m1", 15.5)
    m_dict("123", "p2", 16.0)
    m_dict("456", "m1", 14.0)
    m_dict("456", "i3", 12.5)
# main code
students = []
courses = []
marks = {}
print("> Student Management Program <")
print("===== MENU =====")
while True:
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks")
    print("4. List students")
    print("5. List courses")
    print("6. List marks")
    print("7. Create sample input (for quick testing)")
    print("0. Exit program")
    print("================")
    action = int(input("> What would you like to do?: "))
    # Python doesn't have a built-in switch-case statement :|
    # Note: for actions 7, all lists/dicts are wiped clean and reinit'd. Don't use this if you already used 1, 2 or 3
    if action == 1:
        input_students()
    elif action == 2:
        input_courses()
    elif action == 3:
        input_marks()
    elif action == 4:
        list_students()
    elif action == 5:
        list_courses()
    elif action == 6:
        list_marks()
    elif action == 7:
        testinput()
    else: # if input is 0 or anything else
        break
print("> Program terminated.")

# TODO:
# Validate input type/value for all inputs so program won't quit prematurely
# Input marks for all students instead of just 1 when selecting a course?
# When displaying marks, print actual names for students and courses instead of IDs
