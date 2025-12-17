import math
import numpy as np
import curses as crs
from curses import textpad as txt
# functions
class Student:
    def __init__(self, id, name, dob):
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
    @id.setter
    def id(self, id):
        self.__id = id
    @name.setter
    def name(self, name):
        self.__name = name
    @dob.setter
    def dob(self, dob):
        self.__dob = dob
    def __str__(self):
        return f"{self.__id} | {self.__name} | {self.__dob}"
class Course:
    def __init__(self, id, name, credits):
        self.__id = id
        self.__name = name
        self.__credits = credits
    @classmethod
    def empty(cls):
        return cls("", "")
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def credits(self):
        return self.__credits
    @id.setter
    def id(self, id):
        self.__id = id
    @name.setter
    def name(self, name):
        self.__name = name
    @credits.setter
    def credits(self, credits):
        self.__credits = credits
    def __str__(self):
        return f"{self.id} | {self.name}"
# A Mark object doesn't seem necessary here.
def exit_textbox(key): # generic function for curses module, doesn't belong to any class
    if key == ord("\n"):
        return 7
    return key
class Menu: # advice: consult files in "cursestests" folder
    def __init__(self, stdscr, items):
        self.stdscr = stdscr
        self.items = items
        self.selected = "0"
        self.size = len(items)
    def clearline(self, line): # line: int, y-pos
        self.stdscr.addstr(line, 0, " " * crs.COLS)
    def display(self, y, x): # co-ords of menu relative to stdscr
        self.stdscr.addstr(y, x, "====== MENU ======", crs.A_BOLD)
        for i, item in enumerate(self.items):
            self.stdscr.addstr(y + i + 1, x, item) # the "+1" is for the "=== MENU ===" line
        self.stdscr.refresh()
    def get_action(self, y):
        self.stdscr.addstr(y, 0, "> What would you like to do next?: ", Colors.green)
        self.stdscr.refresh()
        key = self.stdscr.getch()
        self.clearline(y)
        self.stdscr.addstr(y, 0, f"Option {chr(key)} selected.", Colors.green)
        self.stdscr.refresh()
        return key
    def get_text_input(self, y, x): # size of window and relative co-ords
        win_lines = 1
        win_cols = 50 # fixed textbox size.
        win = crs.newwin(win_lines, win_cols, y, x)
        textbox = txt.Textbox(win)
        txt.rectangle(self.stdscr, y - 1, x - 1, y + win_lines, x + win_cols)
        self.stdscr.refresh()
        textbox.edit(exit_textbox)
        text = textbox.gather().strip().replace("\n", "")
        return text
class Colors: # so that methods from other classes can display text with these colors
    green = 0
    yellow = 0
    @staticmethod
    def init_colors():
        crs.init_pair(1, crs.COLOR_GREEN, crs.COLOR_BLACK)
        crs.init_pair(2, crs.COLOR_YELLOW, crs.COLOR_BLACK)
        Colors.green = crs.color_pair(1)
        Colors.yellow = crs.color_pair(2)
class SMS: # Student Management System
    def __init__(self, menu): # Composition - SMS needs to use methods from Menu, but shouldn't be a subclass of it
        self.students = {}
        self.courses = {}
        self.marks = {}
        self.avg_gpa = {}
        self.menu = menu
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
            self.students[s.id] = s
            y -= 1
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
            self.courses[c.id] = c
            y -= 1
        for i in range(y, y + 10):
            self.clearline(i)
        self.stdscr.addstr(y, 0, "Courses information saved.", crs.A_BOLD)
        self.init_marks_table() # add the new courses the marks table
    def init_mark(self, c_id, s_id, mark):
        self.marks[c_id][s_id] = mark
    def init_marks_table(self):
        for c in self.courses:
            if c in self.marks:
                continue
            self.marks[c] = {}
            c_id = self.courses[c].id
            for s in self.students.values():
                self.init_mark(c_id, s.id, "x")
    def input_marks(self, y):
        if self.students == {} or self.courses == {}:
            self.stdscr.addstr(y, 0, "Input students and courses before inputting marks!", Colors.yellow)
            return
        self.display_courses(y)
        y += len(self.courses) + 1
        if self.marks == {}:
            self.init_marks_table()
        while True:
            self.stdscr.addstr(y, 0, "Input course ID to give marks: ", crs.A_BOLD)
            c_id = self.get_text_input(y + 3, 1)
            if c_id in self.courses:
                break
            print("Course not found!")
        self.clearline(y)
        for s in self.students.values():
            while True:
                self.clearline(y)
                self.stdscr.addstr(y, 0, f"Input mark for {s.name} - {s.id}: (\"-\" to skip, \"x\" to clear mark)", crs.A_BOLD)
                mark = self.get_text_input(y + 3, 1)
                if mark == "-":
                    self.stdscr.addstr(y + 1, 0, "Student skipped.", Colors.yellow)
                    break
                elif mark == "x":
                    self.init_mark(c_id, s.id, mark)
                    self.stdscr.addstr(y + 1, 0, "Student's mark cleared.", Colors.yellow)
                    break
                mark = float(mark)
                if mark >= 0 and mark <= 20:
                    mark = float(math.floor(mark * 10)) / 10 # math.floor() doesn't let me specify decimal precision
                    self.init_mark(c_id, s.id, mark)
                    self.clearline(y + 1)
                    self.stdscr.addstr(y + 1, 0, "Student's mark saved.", Colors.yellow)
                    break
                self.clearline(y + 1)
                self.stdscr.addstr(y + 1, 0, "Mark must be in range 0-20!", Colors.yellow)
        y -= len(self.courses) + 1
        for i in range(y, y + len(self.courses) + 10):
            self.clearline(i)
        self.stdscr.addstr(y, 0, "Marks saved.", crs.A_BOLD)
        self.calculate_avg_gpa(0) # recalculating average GPA when the marks are changed
    def display_students(self, y):
        if self.students == {}:
            self.stdscr.addstr(y, 0, "Students list is currently empty.", Colors.yellow)
            return
        self.stdscr.addstr(y, 0, "> Displaying students... ", Colors.yellow)
        for s in self.students:
            y += 1
            self.stdscr.addstr(y, 0, self.students[s].__str__())
    def display_courses(self, y):
        if self.courses == {}:
            self.stdscr.addstr(y, 0, "Courses list is currently empty.", Colors.yellow)
            return
        self.stdscr.addstr(y, 0, "> Displaying courses... ", Colors.yellow)
        for c in self.courses:
            y += 1
            self.stdscr.addstr(y, 0, self.courses[c].__str__())
    def display_marks(self, y): # ohhhhhhhhhhh whatever I'm showing marks for all courses anyway
        if self.marks == {}:
            self.stdscr.addstr(y, 0, "Marks list is currently empty.", Colors.yellow)
            return
        self.stdscr.addstr(y, 0, "> Displaying marks...", Colors.yellow)
        for c in self.marks:
            y += 1
            c_name = [i.name for i in self.courses.values() if i.id == c]
            self.stdscr.addstr(y, 0, f"-> {c_name}:\n ", crs.A_BOLD)
            y += 1
            for s in self.marks[c]:
                s_name = [j.name for j in self.students.values() if j.id == s]
                self.stdscr.addstr(f"{s_name}: {self.marks[c][s]} | ")
    def calculate_avg_gpa(self, y):
        if self.students == {} or self.courses == {} or self.marks == {}:
            self.stdscr.addstr(y, 0, "Not enough data to calculate average GPA!", Colors.yellow)
            return
        for s in self.students:
            credits_list = []
            marks_list = []
            for c in self.courses:
                gpa = self.marks[c][s]
                if gpa != "x":
                    credits_list.append(self.courses[c].credits)
                    marks_list.append(gpa)
            if len(marks_list) == 0: # if (numpy) array is empty
                self.avg_gpa[s] = "x" # placeholder if student doesn't have any individual marks yet
            else:
                self.avg_gpa[s] = np.round(np.average(marks_list, weights=credits_list), decimals=2) # avoid floating point errors
    def display_avg_gpa(self, y):
        if self.avg_gpa == {}:
            self.calculate_avg_gpa(y)
            return
        s_list = []
        g_list = [] # grades
        for s, g in self.avg_gpa.items():
            if g != "x":
                s_list.append(s)
                g_list.append(g)
        s_list = np.array(s_list)
        g_list = np.array(g_list)
        idx = np.argsort(g_list)[::-1]
        s_list = s_list[idx]
        g_list = g_list[idx]
        self.stdscr.addstr(y, 0, "> Students\' GPA sorted in descending order: ", Colors.yellow)
        for i, s in enumerate(s_list):
            s_name = [j.name for j in self.students.values() if j.id == s]
            self.stdscr.addstr(y + 1, 0, f"{s_name}: {g_list[i]}")
            y += 1
    def testinput(self, y):
        if self.students != {} or self.courses != {}:
            self.stdscr.addstr(y, 0, "Cannot use sample input since there is already existing data.", Colors.yellow)
            return
        self.stdscr.addstr(y, 0, "> Creating sample input...", Colors.yellow)
        self.students["111"] = Student("111", "Hien", "24-02-2006")
        self.students["222"] = Student("222", "Khoa", "11-05-1980")
        self.students["333"] = Student("333", "Hoang", "05-11-1976")
        self.students["444"] = Student("444", "Mai", "23-08-2009")
        self.courses["m1"] = Course("m1", "math", 4)
        self.courses["p2"] = Course("p2", "physics", 3)
        self.courses["i3"] = Course("i3", "informatics", 6)
        self.init_marks_table()
        self.init_mark("m1", "111", 15.5)
        self.init_mark("p2", "111", 14.5)
        self.init_mark("i3", "111", 17.8)
        self.init_mark("m1", "222", 16.0)
        self.init_mark("p2", "222", 12.5)
        self.init_mark("m1", "333", 11.5)
        self.init_mark("i3", "333", 16.4)
        self.init_mark("p2", "444", 10.2)
        self.init_mark("i3", "444", 14.7)
        self.calculate_avg_gpa(0) # put input as 0 if there is no chance the method complains about insufficient data

# main code
def main(stdscr):
    menu_items = ["1. Input students",
    "2. Input courses",
    "3. Input marks",
    "4. Display students",
    "5. Display courses",
    "6. Display marks",
    "7. Display sorted GPA list for all students",
    "8. Create sample input for quick testing",
    "0. Exit program"]
    menu = Menu(stdscr, menu_items)
    sms = SMS(menu)
    lines = crs.LINES
    cols = crs.COLS
    mid_line = lines // 2
    mid_col = cols // 2
    Colors.init_colors()
    while True:
        crs.curs_set(0)
        stdscr.clear()
        temp_message = "   Student Management Program (supported by <curses> module)   "
        stdscr.addstr(1, mid_col - len(temp_message) // 2, temp_message, Colors.green | crs.A_BOLD)
        menu.display(2, 0)
        stdscr.keypad(True)
        linepos = menu.size + 3
        action = menu.get_action(linepos)
        crs.curs_set(1)
        linepos += 1
        if action == ord("1"):
            sms.input_students(linepos)
        elif action == ord("2"):
            sms.input_courses(linepos)
        elif action == ord("3"):
            sms.input_marks(linepos)
        elif action == ord("4"):
            sms.display_students(linepos)
        elif action == ord("5"):
            sms.display_courses(linepos)
        elif action == ord("6"):
            sms.display_marks(linepos)
        elif action == ord("7"):
            sms.display_avg_gpa(linepos)
        elif action == ord("8"):
            sms.testinput(linepos)
        elif action == ord("0"):
            break
        else:
            stdscr.addstr(linepos + 1, 0, "Not a valid action. Please try again.", Colors.yellow)
        stdscr.addstr(linepos - 1, 0, "Press any key to continue...", Colors.green)
        stdscr.refresh()
        stdscr.getch()
    stdscr.clear()
    temp_message = "Terminating program..."
    for i in range(3, 8):
        stdscr.addstr(i, mid_col - len(temp_message) // 2, temp_message, Colors.green)
        stdscr.refresh()
        crs.napms(50)
    crs.napms(250)
    # and then the program terminates!

crs.wrapper(main)
