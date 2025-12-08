# functions
class Student:
    def __init__(self, id, name, dob): # call this function using class name
            self.__id = id
            self.__name = name
            self.__dob = dob
    @classmethod
    def empty(cls):
        return cls("", "", "")
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def dob(self):
        return self.__dob
    def input(self):
        self.id = input("ID: ")
        self.name = input("Name: ")
        self.dob = input("Date of birth (dd-MM-YYYY): ")
    def __str__(self):
        return f"{self.__id} | {self.__name} | {self.__dob}"
class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    @classmethod
    def empty(cls):
        return cls("", "")
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    def input(self):
        self.id = input("ID: ")
        self.name = input("Name: ")
    def __str__(self):
        return f"{self.id} | {self.name}"
# A Mark object doesn't seem necessary here.
class SMS: # Student Management System
    def __init__(self):
        self.students = {} # students & courses are now dicts, easier for storing objects
        self.courses = {}
        self.marks = {}
        # since these dicts are only used in the class itself, encapsulation isn't necessary.
    def input_students(self):
        while True:
            student_amt = int(input("Input amount of students: "))
            if student_amt >= 0:
                break
            print("Invalid amount of students!")
        for i in range (student_amt):
            s = Student.empty()
            print(f"Input information for student {i+1}...")
            s.input()
            self.students[s.id] = s
    def input_courses(self):
        while True:
            course_amt = int(input("Input amount of courses: "))
            if course_amt >= 0:
                break
            print("Invalid amount of courses!")
        for i in range (course_amt):
            c = Course.empty()
            print(f"Input information for course {i+1}...")
            c.input()
            self.courses[c.id] = c
    def init_mark(self, c_id, s_id, mark): # student->course->mark order changed compared to practice 1
        self.marks[c_id][s_id] = mark
    def init_marks_table(self): # this function modifies self.marks directly instead of returning a init'd marks table
        self.marks = {}
        for c in self.courses:
            self.marks[c] = {}
            c_id = self.courses[c].id
            for s in self.students.values():
                self.init_mark(c_id, s.id, "x")
    def input_marks(self):
        if self.students == {} or self.courses == {}:
            print("Input students and courses before inputting marks!")
            return
        self.display_courses()
        if self.marks == {}:
            self.init_marks_table()
        while True:
            c_id = input("Input course ID to give marks: ")
            if c_id in self.courses:
                break
            print("Course not found!")
        for s in self.students.values():
            while True:
                mark = input(f"Input mark for {s.name} ({s.id}): ")
                if mark == "x":
                    print("Student skipped.")
                    break
                mark = float(mark)
                if mark >= 0 and mark <= 20:
                    self.init_mark(c_id, s.id, mark)
                    break
                print("Mark must be in range 0-20!")
    def display_students(self):
        if self.students == {}:
            print("Students list is currently empty.")
            return
        print("> Displaying students... ")
        for s in self.students:
            print(self.students[s])
    def display_courses(self):
        if self.courses == {}:
            print("Courses list is currently empty.")
            return
        print("> Displaying courses... ")
        for c in self.courses:
            print(self.courses[c])
    def display_marks(self): # ohhhhhhhhhhh whatever I'm showing marks for all courses anyway
        if self.marks == {}:
            print("Marks list is currently empty.")
            return
        print(f"> Displaying marks...")
        for c in self.marks:
            c_name = [i.name for i in self.courses.values() if i.id == c]
            print(f"{c_name}: ")
            for s in self.marks[c]:
                s_name = [j.name for j in self.students.values() if j.id == s]
                print(f"{s_name}: {self.marks[c][s]} | ", end = "")
            print("") # insert newline between students
    def testinput(self):
        if self.students != {} or self.courses != {}:
            print("Cannot use sample input since there is already data in (students) or (courses).")
            return
        print("> Creating sample input...")
        self.students["123"] = Student("123", "Hien", "24-02-2006")
        self.students["456"] = Student("456", "Khoa", "11-05-1980")
        self.courses["m1"] = Course("m1", "math")
        self.courses["p2"] = Course("p2", "physics")
        self.courses["i3"] = Course("i3", "informatics")
        self.init_marks_table()
        self.init_mark("m1", "123", 15.5)
        self.init_mark("i3", "123", 17.8)
        self.init_mark("m1", "456", 14.0)
        self.init_mark("p2", "456", 12.5)
# main code
manager = SMS()
print("> Student Management Program [OOP version] <")
while True:
    print("====== MENU ======")
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks")
    print("4. Display students")
    print("5. Display courses")
    print("6. Display marks")
    print("7. Create sample input (for quick testing)")
    print("0. Exit program")
    action = input("> What would you like to do?: ")
    # Note: for actions 7, all displays/dicts are wiped clean and reinit'd. Don't use this if you already used 1, 2 or 3
    if action == "1":
        manager.input_students()
    elif action == "2":
        manager.input_courses()
    elif action == "3":
        manager.input_marks()
    elif action == "4":
        manager.display_students()
    elif action == "5":
        manager.display_courses()
    elif action == "6":
        manager.display_marks()
    elif action == "7":
        manager.testinput()
    elif action == "0":
        break
    else:
        print("Not a valid action. Please try again.")
print("> Program terminated.")
