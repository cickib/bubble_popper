import curses
import time
import random
from curses import wrapper
import rocket

screen = curses.initscr()

curses.noecho()
curses.curs_set(0)
begin_x = 0
begin_y = 0
height = 100
width = 300
win = curses.newwin(height, width, begin_y, begin_x)
win_small = curses.newwin(height-1, width-1, begin_y+1, begin_x+1)
win.border(0)
win.keypad(1)
win.nodelay(1)
title = "Bubble Popper"
win.addstr(0, (curses.COLS - len(title)) // 2, title) #nem műkszik
win_small.keypad(1)
win_small.nodelay(1)



printable_num = list(c for c in range(48, 58))
printable_num.append(27)

key = 48
    
count = 0

while key != 27:

    if count % 10 == 0 :
        x = random.randint(0, 2)
        num_y = 1
        num_x = random.randint(10, 70)
        win_small.addstr(num_y, num_x, str(rocket.rockets[x][0]))
        win_small.addstr(num_y+1, num_x, str(rocket.rockets[x][1]))
        win_small.addstr(num_y+2, num_x, str(rocket.rockets[x][2]))
    #coord = [num_y, num_x)
    win_small.timeout(100)
    count += 1

    event = win_small.getch()
    if event == printable_num[len(printable_num)-1]:
        break

    if (event-48) == x:
        #curses.getsyx(num_y, num_x)
        #win.delch(num_y, num_x)
        win_small.clear()

    #elif event == printable_num[0]:
    #event = screen.getch()

    if event in printable_num:
        key = event

    #if event ==
#        snake = [[4,10]]
#        title = ' Hello snake! '
#        win.addstr(0, (curses.COLS - len(title)) // 2, title)

#while key != 27:            # not Esc is pressed
#        win.timeout(100)        # wait 0.1 sec

#        event = win.getch()     # get the code of pressed key (if nothing pressed, this returns -1)
#        if event in printable_num:
#            key = event
#curses.wrapper()
curses.endwin()
