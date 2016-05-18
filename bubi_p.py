import curses
import time
import random
screen = curses.initscr()

printable_num = list(c for c in range(48, 58))
printable_num.append(27)

def newNum():
    x = random.randint(0, 9)
    num_y = 0
    num_x = 0
    screen.addstr(num_y, num_x, str(x))
    #screen.move(10 ,10)
    print(x)

def popping():
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
    win.addstr(0, (curses.COLS - len(title)) // 2, title) #ide rakja a feliratot, középre igazítva

    key = 48
    newNum()
    while key != 27:
        win.timeout(300)
        event = win.getch()
        if event == printable_num[len(printable_num)-1]:
            break
        elif event == printable_num[0]:
            win.addstr(str(newNum()))
        #event = screen.getch()


        if event in printable_num:
            key = event
            print(key - 48)
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
newNum()
popping()
curses.endwin()
