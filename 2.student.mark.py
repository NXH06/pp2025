# functions
class Student:
    def __init__(self, id, name, dob):
        self.id = ""
        self.name = ""
        self.dob = ""
    def input(self):
        self.id = input(f"Input ID of student {i + 1}: ") # Avoid zero-indexing while printing
        self.name = input(f"Input name of student {i + 1}: ")
        self.dob = input(f"Input date of birth (YYYY-MM-dd) of student {i + 1}: ")
    def display(self):
        print(f"{self.id} | {self.name} | {self.dob}")    
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
class Mark(Student, Course):
    def __init__(self, s_obj, c_obj, mark):
        self.s_id = s_obj
        self.c_id = c_obj
        self.mark = mark
class SMS: # Student Management System
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
    def input_students(self):
        while True:
            student_amt = int(input("Input amount of students: "))
            if student_amt >= 0:
                break
            print("Invalid amount of students!")
        for i in range (student_amt):
            s = Student()
            s.input()
            self.students.append(s)
    def input_courses(self):
        while True:
            course_amt = int(input("Input amount of courses: "))
            if course_amt >= 0:
                break
            print("Invalid amount of courses!")
        for i in range (course_amt):
            c_id = input(f"Input ID of course {i + 1}: ")
            c_name = input(f"Input name of course {i + 1}: ")
            new_course = Course(c_id, c_name)
            self.courses.append(new_course)
        return courses
    def init_marks(self): # make 2D table of marks, all filled with placeholder values
        for s in self.students:
            s_id = s["id"]
            marks[s_id] = {}
            for c in self.courses:
                c_id = c["id"]
                Mark.m_dict(s_id, c_id, "x") # placeholder value if the student doesn't have any marks in that course
    def input_marks(self):
        self.display_courses()
        if students == [] or courses == []:
            print("Input students and courses before inputting marks!")
            return
        if marks == {}:
            self.init_marks()
        while True:
            c_id = input("Input course ID to give marks: ")
            if any(c_id == c["id"] for c in courses): # bool "any" returns True if any element in iterable object is true
                break
            print("Course not found!")
        while True:
            s_id = input("Input student ID to give marks: ")
            if any(s_id == s["id"] for s in students):
                break
            print("Student not found!")
        while True:
            mark = float(input("Input mark: "))
            if mark >= 0 and mark <= 20:
                break
            print("Mark must be in range 0-20!")
        Marks.m_dict(s_id, c_id, mark)
    def display_students(self):
        if self.students == []:
            print("Students display is currently empty.")
            return
        print("> Displaying students... ")
        for s in self.students:
            s.display()
    def display_courses(self):
        if self.courses == []:
            print("Courses display is currently empty.")
            return
        print("> Displaying courses... ")
        for i in range (len(self.courses)):
            print(self.courses[i])
    def display_marks(self):
        if self.marks == {}:
            print("Marks display is currently empty.")
            return
        print("> Displaying marks...")
        for student in self.marks:
            print(f"{student}: {marks[student]}")

# Function for a quick sample input (for code testing purposes). Working with command-line only is too slow...
def testinput():
    global students, courses, marks
    if students != [] or courses != []:
        print("Cannot use sample input since there is already data in [students] or [courses].")
        return
    print("> Creating sample input...")
    students = [Student.s_dict("123", "Hien", "2006-02-24"), Student.s_dict("456", "Khoa", "1980-05-11")]
    courses = [Course.c_dict("m1", "math"), Course.c_dict("p2", "physics"), Course.c_dict("i3", "informatics")]
    marks = init_marks()
    Marks.m_dict("123", "m1", 15.5)
    Marks.m_dict("123", "p2", 16.0)
    Marks.m_dict("456", "m1", 14.0)
    Marks.m_dict("456", "i3", 12.5)
# main code
print("> Student Management Program <")
print("====== MENU ======")
while True:
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks")
    print("4. Display students")
    print("5. Display courses")
    print("6. Display marks")
    print("7. Create sample input (for quick testing)")
    print("0. Exit program")
    print("==================")
    action = int(input("> What would you like to do?: "))
    # Python doesn't have a built-in switch-case statement :|
    # Note: for actions 7, all displays/dicts are wiped clean and reinit'd. Don't use this if you already used 1, 2 or 3
    if action == 1:
        input_students()
    elif action == 2:
        input_courses()
    elif action == 3:
        input_marks()
    elif action == 4:
        display_students()
    elif action == 5:
        display_courses()
    elif action == 6:
        display_marks()
    elif action == 7:
        testinput()
    elif action == 0:
        break
    else:
        print("Not a valid action. Please try again.")
    print("==================")
print("> Program terminated.")

# TODO:
# Input marks for all students instead of just 1 when selecting a course?
# When displaying marks, print actual names for students and courses instead of IDs
