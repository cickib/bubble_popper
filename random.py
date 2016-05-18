import curses
import time
import random
screen = curses.initscr()

curses.noecho()
curses.curs_set(0)
begin_x = 0
begin_y = 0
height = 100
width = 300
win = curses.newwin(height, width, begin_y, begin_x)
win.keypad(1)
win.nodelay(1)
title = "Bubble Popper"
win.addstr(0, (curses.COLS - len(title)) // 2, title)

def newNum():
    x = random.randint(0, 9)
    num_y = 0
    num_x = 0
    screen.addstr(num_y, num_x, str(x))
    print(x)

newNum()
