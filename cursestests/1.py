import curses as crs
from curses import textpad as txt

def exit_textbox(key):
    if key == ord("\n"):
        return 7 # ASCII ID of Ctrl+G, which exits textbox
    return key
def main(stdscr):
    stdscr.clear()
    crs.init_pair(1, crs.COLOR_YELLOW, crs.COLOR_BLUE)
    yellow_blue = crs.color_pair(1)
    lines = crs.LINES
    cols = crs.COLS
    mid_line = lines // 2 # integer division!
    mid_col = cols // 2
    menu_items = ["Option 1", "Option 2", "Option 3", "Option 4", "EXIT"]
    menu_len = len(menu_items)
    selected = 0
    while True:
        crs.curs_set(0) # disable the blinking cursor
        stdscr.clear()
        for i, item in enumerate(menu_items): # enumerate: (index, element) of list
            if i == selected:
                stdscr.addstr(i, mid_col, f"{item}", crs.A_REVERSE)
            else:
                stdscr.addstr(i, mid_col, item)
        key = stdscr.getch()
        if key == crs.KEY_UP and selected > 0:
            selected -= 1
        elif key == crs.KEY_DOWN and selected < len(menu_items) - 1:
            selected += 1
        elif key == ord("\n"):
            for i in range(1, 3): # remember, the iteration stops right before the end
                stdscr.addstr(menu_len + i, 0, " " * cols) # clear line by overwriting line with all blanks!
            stdscr.addstr(menu_len + 1, mid_col // 2, f"> You selected [{menu_items[selected]}]", crs.A_BOLD)
            stdscr.refresh()
            if selected == menu_len - 1:
                stdscr.addstr(menu_len + 2, mid_col // 2, "TERMINATING PROGRAM...\n", yellow_blue)
                stdscr.refresh()
                crs.napms(1000)
                break
            stdscr.addstr(menu_len + 2, mid_col // 2, "What would you like to change the option's name to?")
            # stdscr.refresh()
            win_y = 10
            win_x = mid_col // 2
            win_lines = 1
            win_cols = 40
            win = crs.newwin(win_lines, win_cols, win_y, win_x)
            textbox = txt.Textbox(win)
            txt.rectangle(stdscr, win_y - 1, win_x - 1, win_y + win_lines, win_x + win_cols)
            # note: if txt.rectangle was drawn inside win, the user input gets pushed down by the rectangle instead of appearing inside it
            stdscr.refresh()
            crs.curs_set(1) # enable blinking cursor for text input
            textbox.edit(exit_textbox)
            text = textbox.gather().strip().replace("\n", "") # can use text = textbox.edit() directly
            menu_items[selected] = text
        stdscr.refresh()

crs.wrapper(main)