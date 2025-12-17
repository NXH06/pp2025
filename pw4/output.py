import curses as crs
import numpy as np

class Colors:
    green = 0
    yellow = 0
    def init_colors():
        crs.init_pair(1, crs.COLOR_GREEN, crs.COLOR_BLACK)
        crs.init_pair(2, crs.COLOR_YELLOW, crs.COLOR_BLACK)
        Colors.green = crs.color_pair(1)
        Colors.yellow = crs.color_pair(2)
class OutputHandler:
    def __init__(self, menu, sms):
        self.menu = menu
        self.sms = sms
        self.stdscr = menu.stdscr
    def clearline(self, line):
        return self.menu.clearline(line)
    def display_students(self, y):
            if self.sms.students == {}:
                self.stdscr.addstr(y, 0, "Students list is currently empty.", Colors.yellow)
                return
            self.stdscr.addstr(y, 0, "> Displaying students... ", Colors.yellow)
            for s in self.sms.students:
                y += 1
                self.stdscr.addstr(y, 0, self.sms.students[s].__str__())
    def display_courses(self, y):
        if self.sms.courses == {}:
            self.stdscr.addstr(y, 0, "Courses list is currently empty.", Colors.yellow)
            return
        self.stdscr.addstr(y, 0, "> Displaying courses... ", Colors.yellow)
        for c in self.sms.courses:
            y += 1
            self.stdscr.addstr(y, 0, self.sms.courses[c].__str__())
    def display_marks(self, y):
        if self.sms.marks == {}:
            self.stdscr.addstr(y, 0, "Marks list is currently empty.", Colors.yellow)
            return
        self.stdscr.addstr(y, 0, "> Displaying marks...", Colors.yellow)
        for c in self.sms.marks:
            y += 1
            c_name = [i.name for i in self.sms.courses.values() if i.id == c]
            self.stdscr.addstr(y, 0, f"-> {c_name}:\n ", crs.A_BOLD)
            y += 1
            for s in self.sms.marks[c]:
                s_name = [j.name for j in self.sms.students.values() if j.id == s]
                self.stdscr.addstr(f"{s_name}: {self.sms.marks[c][s]} | ")
    def display_avg_gpa(self, y):
        if self.sms.avg_gpa == {}:
            self.calculate_avg_gpa(y)
            return
        s_list = []
        g_list = []
        for s, g in self.sms.avg_gpa.items():
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
            s_name = [j.name for j in self.sms.students.values() if j.id == s]
            self.stdscr.addstr(y + 1, 0, f"{s_name}: {g_list[i]}")
            y += 1