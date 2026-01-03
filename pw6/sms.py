import numpy as np
from output import Colors

class SMS: # note: don't import this class anywhere, just init a "sms" object
    def __init__(self, menu):
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