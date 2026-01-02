import curses as crs
from menu import Menu
from sms import SMS
from input import InputHandler
from output import OutputHandler, Colors
import zipfile as zf
import os
from os.path import exists
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
    input = InputHandler(menu, sms)
    output = OutputHandler(menu, sms)
    lines = crs.LINES
    cols = crs.COLS
    mid_line = lines // 2
    mid_col = cols // 2
    Colors.init_colors()
    if exists("students.dat"):
        stdscr.addstr(0, 0, "File students.dat found, extracting information...", Colors.green)
        stdscr.refresh()
        with zf.ZipFile("students.dat", "r") as zipf:
            zipf.extractall()
        crs.napms(250)
    while True:
        crs.curs_set(0)
        stdscr.clear()
        temp_message = "Student Management Program (supported by <curses> module)"
        stdscr.addstr(1, mid_col - len(temp_message) // 2, temp_message, Colors.green | crs.A_BOLD)
        menu.display(2, 0)
        stdscr.keypad(True)
        linepos = menu.size + 3
        action = menu.get_action(linepos)
        crs.curs_set(1)
        linepos += 1
        if action == ord("1"):
            input.input_students(linepos)
        elif action == ord("2"):
            input.input_courses(linepos)
        elif action == ord("3"):
            input.input_marks(linepos)
        elif action == ord("4"):
            output.display_students(linepos)
        elif action == ord("5"):
            output.display_courses(linepos)
        elif action == ord("6"):
            output.display_marks(linepos)
        elif action == ord("7"):
            output.display_avg_gpa(linepos)
        elif action == ord("8"):
            input.testinput(linepos)
        elif action == ord("0"):
            menu.clearline(linepos)
            stdscr.addstr(linepos, 0, "Compressing and saving information...", Colors.green)
            stdscr.refresh()
            with zf.ZipFile("students.dat", "w") as zipf:
                try:
                    zipf.write("students.txt")
                    zipf.write("courses.txt")
                    zipf.write("marks.txt")
                    os.remove("students.txt")
                    os.remove("courses.txt")
                    os.remove("marks.txt")
                    crs.napms(250)
                    break
                except IOError:
                    stdscr.addstr(linepos + 1, 0, "Output file(s) not found! Quit anyway? (press y if yes) ", Colors.yellow)
                    stdscr.refresh()
                    crs.curs_set(0)
                    key = stdscr.getch()
                    if key == ord("y"):
                        break
                    else:
                        menu.clearline(linepos)
                        menu.clearline(linepos + 1)
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