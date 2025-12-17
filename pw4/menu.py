import curses as crs
from curses import textpad as txt
from output import Colors

def exit_textbox(key):
    if key == ord("\n"):
        return 7
    return key
class Menu: # note: don't import this class anywhere, just init a "menu" object
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