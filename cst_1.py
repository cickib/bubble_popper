import curses
import time
import random
from curses import wrapper

screen = curses.initscr()

curses.noecho()
curses.curs_set(0)
begin_x = 0
begin_y = 0
height = 100
width = 100
win = curses.newwin(height, width, begin_y, begin_x)
win_small = curses.newwin(100, 200, 10, 10)
win.keypad(1)
win_small.keypad(1)
win.nodelay(1)
win_small.nodelay(1)


printable_num = list(c for c in range(48, 58))
printable_num.append(27)







key = 48

win_small.clear()


count = 0

while key != 27:

    if count % 20 == 0:
        x = random.randint(0, 2)
        num_y = random.randint(1, 50)
        num_x = random.randint(1, 50)
        win_small.addstr(num_y, num_x, str(x))
    #coord = [num_y, num_x)
    win_small.timeout(20)
    count += 1

    event = win_small.getch()
    if event == printable_num[len(printable_num)-1]:
        break


    if (event-48) == x:
        #curses.getsyx(num_y, num_x)
        #win_small.delch(num_y, num_x)
        #win_smallrefresh()
        win_small.clear()

    #elif event == printable_num[0]:

    #event = screen.getch()


    if event in printable_num:
        key = event

    #if event ==

#key = 48
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
