import curses
import time
import random
screen = curses.initscr()

printable_num = list(c for c in range(48, 58))
printable_num.append(27)

def newNum():
    rand_num = random.randint(0, 9)
    num_y = 0
    num_x = 0
    screen.addstr(num_y, num_x, str(rand_num))
    #screen.move(10 ,10)

def match():
    global key
    global rand_num
    for n in range(1, ((len(printable_num)))-1):
        printable_num[n-1] = key
    answer = key - 48
    if rand_num == answer:
        screen.addstr("The User Pressed Lower Case p")

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
    win.addstr(0, (curses.COLS - len(title)) // 2, title)

    key = 48

    while key != 27:
        win.timeout(500)
        event = win.getch()
        if event == printable_num[len(printable_num)-1]:
            break
        # if event in printable_num:
        #     key = event



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
