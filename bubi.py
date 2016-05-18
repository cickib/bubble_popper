import curses
from curses import wrapper
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr = curses.initscr()
begin_x = 0
begin_y = 0
height = 10
width = 30
win = curses.newwin(height, width, begin_y, begin_x)

#curses.endwin()
