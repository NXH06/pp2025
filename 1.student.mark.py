from prettytable import PrettyTable
# functions
def input_students():
    global students
    while True:
        student_amt = int(input("Input amount of students: "))
        if student_amt >= 0:
            break
        print("Invalid amount of students!")
    for i in range (student_amt):
        print(f"Input information for student {i+1}...") # Avoid zero-indexing while printing
        s_id = input("ID: ").strip().upper()
        s_name = input("Name: ")
        s_dob = input("Date of birth (dd-MM-YYYY): ")
        students.append(s_dict(s_id, s_name, s_dob))
def input_courses():
    global courses
    while True:
        course_amt = int(input("Input amount of courses: "))
        if course_amt >= 0:
            break
        print("Invalid amount of courses!")
    for i in range (course_amt):
        print(f"Input information for course {i+1}...") # Avoid zero-indexing while printing
        c_id = input("ID: ").strip().upper()
        c_name = input("Name: ")
        courses.append(c_dict(c_id, c_name))
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
    display_courses()
    if students == [] or courses == []:
        print("Input students and courses before inputting marks!")
        return
    if marks == {}:
        marks = init_marks()
    while True:
        c_id = input("Input course ID to give marks: ")
        if any(c_id == c["id"] for c in courses): # bool "any" returns True if any element in iterable object is true
            break
        print("Course not found!")
    for s in students:
        while True:
            mark = input(f"Input mark for {s["name"]} ({s["id"]}): ")
            if mark == "x":
                print("Student skipped.")
                break
            mark = float(mark)
            if mark >= 0 and mark <= 20:
                m_dict(s["id"], c_id, mark)
                break
            print("Mark must be in range 0-20!")
def display_students():
    if students == []:
        print("Students display is currently empty.")
        return
    print("> Displaying students...\n")
    for s in students:
        print(f"{s["id"]} | {s["name"]} | {s["dob"]}") 
def display_courses():
    if courses == []:
        print("Courses display is currently empty.")
        return
    print("> Displaying courses...\n")
    for c in courses:
        print(f"{c["id"]} | {c["name"]}")
def display_marks():
    if marks == {}:
        print("Marks display is currently empty.")
        return
    print("> Displaying marks...\n")
    for s in marks:
        s_name = [i["name"] for i in students if i["id"] == s] # iterate through [students] for matching id, then return name
        print(f"{s_name}: {marks[s]}")
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
    students = [s_dict("123", "Hien", "24-02-2006"), s_dict("456", "Khoa", "11-05-1980")]
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
while True:
    print("\n====== MENU ======")
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks")
    print("4. Display students")
    print("5. Display courses")
    print("6. Display marks")
    print("7. Create sample input (for quick testing)")
    print("0. Exit program")
    print("==================")
    action = input("> What would you like to do?: ").strip()
    # Python doesn't have a built-in switch-case statement :|
    # Note: for actions 7, all displays/dicts are wiped clean and reinit'd. Don't use this if you already used 1, 2 or 3
    if action == "1":
        input_students()
    elif action == "2":
        input_courses()
    elif action == "3":
        input_marks()
    elif action == "4":
        display_students()
    elif action == "5":
        display_courses()
    elif action == "6":
        display_marks()
    elif action == "7":
        testinput()
    elif action == "0":
        break
    else:
        print("Not a valid action. Please try again.")
print("> Program terminated.")

# TODO:
# Input marks for all students instead of just 1 when selecting a course?
# When displaying marks, print actual names for students and courses instead of IDs
