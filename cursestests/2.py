import curses as crs

def main(stdscr):
    stdscr.clear()
    crs.init_pair(1, crs.COLOR_YELLOW, crs.COLOR_BLUE)
    yellow_blue = crs.color_pair(1)
    linepos = 1
    while True:
        stdscr.addstr(0, 0, "Press any key...")
        stdscr.refresh()
        key = stdscr.getch()
        stdscr.addstr(linepos, 0, f"You pressed {chr(key)}, which is keycode {key}.", yellow_blue)
        stdscr.refresh()
        linepos += 1
        if key == ord("z"):
            stdscr.addstr(linepos + 2, 10, "KILLING PROGRAM...")
            stdscr.refresh()
            crs.napms(1000)
            crs.endwin()
            break

crs.wrapper(main)
