import curses as crs
from menu import Menu
from sms import SMS
from input_handler import InputHandler
from output_handler import OutputHandler, Colors

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