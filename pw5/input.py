import curses as crs
import math
from domains.student import Student
from domains.course import Course
from output import Colors

class InputHandler:
    def __init__(self, menu, sms):
        self.menu = menu
        self.sms = sms
        self.stdscr = menu.stdscr
    def clearline(self, line):
        return self.menu.clearline(line)
    def get_text_input(self, y, x):
        return self.menu.get_text_input(y, x)
    def input_students(self, y):
        while True:
            self.stdscr.addstr(y, 0, "Input amount of students: ", crs.A_BOLD)
            student_amt = int(self.get_text_input(y + 3, 1)) # x = 1, since txt.rectangle draw left side at x - 1
            if student_amt >= 0:
                break
            self.stdscr.addstr(y + 1, 0, "Invalid amount of students!", Colors.yellow)
        for i in range(y, y + 10):
            self.clearline(i)
        for i in range (student_amt):
            self.stdscr.addstr(y, 0, f"Input information for student {i+1}...", Colors.yellow)
            y += 1
            self.clearline(y)
            self.stdscr.addstr(y, 0, "ID: ")
            id = self.get_text_input(y + 3, 1)
            self.clearline(y)
            self.stdscr.addstr(y, 0, "Name: ")
            name = self.get_text_input(y + 3, 1)
            self.clearline(y)
            self.stdscr.addstr(y, 0, "Date of birth (dd-mm-yyyy): ")
            dob = self.get_text_input(y + 3, 1)
            s = Student(id, name, dob)
            self.sms.students[s.id] = s
            y -= 1
        with open("students.txt", "w") as f:
            for s in self.sms.students.values():
                f.write(f"{s.__str__()}\n")
        # no need to check for "file doesn't exist" exception since "w" mode creates file in that case anyway
        for i in range(y, y + 10):
            self.clearline(i)
        self.stdscr.addstr(y, 0, "Students information saved.", crs.A_BOLD)
    def input_courses(self, y):
        while True:
            self.stdscr.addstr(y, 0, "Input amount of courses: ", crs.A_BOLD)
            course_amt = int(self.get_text_input(y + 3, 1))
            if course_amt >= 0:
                break
            self.stdscr.addstr(y + 1, 0, "Invalid amount of courses!", Colors.yellow)
        for i in range(y, y + 10):
            self.clearline(i)
        for i in range (course_amt):
            self.stdscr.addstr(y, 0, f"Input information for course {i+1}...", Colors.yellow)
            y += 1
            self.clearline(y)
            self.stdscr.addstr(y, 0, "ID: ")
            id = self.get_text_input(y + 3, 1)
            self.clearline(y)
            self.stdscr.addstr(y, 0, "Name: ")
            name = self.get_text_input(y + 3, 1)
            self.clearline(y)
            self.stdscr.addstr(y, 0, "Amount of credits: ")
            credits = int(self.get_text_input(y + 3, 1))
            c = Course(id, name, credits)
            self.sms.courses[c.id] = c
            y -= 1
        with open("courses.txt", "w") as f:
            for c in self.sms.courses.values():
                f.write(f"{c.__str__()}\n")
        for i in range(y, y + 10):
            self.clearline(i)
        self.stdscr.addstr(y, 0, "Courses information saved.", crs.A_BOLD)
        self.sms.init_marks_table() # add the new courses the marks table
    def input_marks(self, y):
        if self.sms.students == {} or self.sms.courses == {}:
            self.stdscr.addstr(y, 0, "Input students and courses before inputting marks!", Colors.yellow)
            return
        from output import OutputHandler
        output = OutputHandler(self.menu, self.sms)
        output.display_courses(y)
        y += len(self.sms.courses) + 1
        if self.sms.marks == {}:
            self.sms.init_marks_table()
        while True:
            self.stdscr.addstr(y, 0, "Input course ID to give marks: ", crs.A_BOLD)
            c_id = self.get_text_input(y + 3, 1)
            if c_id in self.sms.courses:
                break
            self.stdscr.addstr(y + 1, 0, "Course not found!", Colors.yellow)
        self.clearline(y)
        self.clearline(y + 1)
        for s in self.sms.students.values():
            while True:
                self.clearline(y)
                self.stdscr.addstr(y, 0, f"Input mark for {s.name} - {s.id}: (\"-\" to skip, \"x\" to clear mark)", crs.A_BOLD)
                mark = self.get_text_input(y + 3, 1)
                if mark == "-":
                    self.clearline(y + 1)
                    self.stdscr.addstr(y + 1, 0, "Student skipped.", Colors.yellow)
                    break
                elif mark == "x":
                    self.sms.init_mark(c_id, s.id, mark)
                    self.clearline(y + 1)
                    self.stdscr.addstr(y + 1, 0, "Student's mark cleared.", Colors.yellow)
                    break
                mark = float(mark)
                if mark >= 0 and mark <= 20:
                    mark = float(math.floor(mark * 10)) / 10
                    self.sms.init_mark(c_id, s.id, mark)
                    self.clearline(y + 1)
                    self.stdscr.addstr(y + 1, 0, "Student's mark saved.", Colors.yellow)
                    break
                self.stdscr.addstr(y + 1, 0, "Mark must be in range 0-20!", Colors.yellow)
        with open("marks.txt", "w") as f:
            for c in self.sms.marks:
                for m, i in enumerate(self.sms.marks[c].values()):
                    f.write(f"{m}")
                    if i < len(self.sms.marks[c].values()) - 1: # don't write pipe after last mark of course
                        f.write(" | ")
                f.write("\n")
        y -= len(self.sms.courses) + 1
        for i in range(y, y + len(self.sms.courses) + 10):
            self.clearline(i)
        self.stdscr.addstr(y, 0, "Marks saved.", crs.A_BOLD)
        self.sms.calculate_avg_gpa(0) # recalculating average GPA when the marks are changed
    def testinput(self, y):
        if self.sms.students != {} or self.sms.courses != {}:
            self.stdscr.addstr(y, 0, "Cannot use sample input since there is already existing data.", Colors.yellow)
            return
        self.stdscr.addstr(y, 0, "> Creating sample input...", Colors.yellow)
        self.sms.students["111"] = Student("111", "Hien", "24-02-2006")
        self.sms.students["222"] = Student("222", "Khoa", "11-05-1980")
        self.sms.students["333"] = Student("333", "Hoang", "05-11-1976")
        self.sms.students["444"] = Student("444", "Mai", "23-08-2009")
        self.sms.courses["m1"] = Course("m1", "math", 4)
        self.sms.courses["p2"] = Course("p2", "physics", 3)
        self.sms.courses["i3"] = Course("i3", "informatics", 6)
        self.sms.init_marks_table()
        self.sms.init_mark("m1", "111", 15.5)
        self.sms.init_mark("p2", "111", 14.5)
        self.sms.init_mark("i3", "111", 17.8)
        self.sms.init_mark("m1", "222", 16.0)
        self.sms.init_mark("p2", "222", 12.5)
        self.sms.init_mark("m1", "333", 11.5)
        self.sms.init_mark("i3", "333", 16.4)
        self.sms.init_mark("p2", "444", 10.2)
        self.sms.init_mark("i3", "444", 14.7)
        self.sms.calculate_avg_gpa(0)
        with open("students.txt", "w") as f:
            for s in self.sms.students.values():
                f.write(f"{s.__str__()}\n")
        with open("courses.txt", "w") as f:
            for c in self.sms.courses.values():
                f.write(f"{c.__str__()}\n")
        with open("marks.txt", "w") as f:
            for c in self.sms.marks:
                for m, i in enumerate(self.sms.marks[c].values()):
                    f.write(f"{m}")
                    if i < len(self.sms.marks[c].values()) - 1:
                        f.write(" | ")
                f.write("\n")
    def read_from_file(self):
        try:
            with open("students.txt", "r") as f:
                while True:
                    line = f.readline()
                    if line == "": # end of file
                        break
                    s = line.split(" | ")
                    for i in s:
                        i = i.strip()
                    self.sms.students[s[0]] = Student(s[0], s[1], s[2])
            with open("courses.txt", "r") as f:
                while True:
                    line = f.readline()
                    if line == "": # end of file
                        break
                    c = line.split(" | ")
                    for i in c:
                        i = i.strip()
                    self.sms.courses[c[0]] = Course(c[0], c[1], int(c[2])) # amount of credits is an integer
            with open("marks.txt", "r") as f:
                self.sms.init_marks_table()
                for c in self.sms.courses:
                    line = f.readline()
                    line = line.split(" | ")
                    for m, s in zip(line, self.sms.students):
                        m = m.strip()
                        if m != "x":
                            m = float(m)
                        self.sms.marks[c][s] = m
        except IOError:
            self.stdscr.addstr(1, 0, "Input files missing! Stopping extraction...", Colors.yellow)
            self.stdscr.refresh()