import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

# end the program
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
