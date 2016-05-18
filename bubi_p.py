import curses
import time
import random
screen = curses.initscr()

printable_num = list(c for c in range(48, 58))
printable_num.append(27)
print(printable_num)
print(type(printable_num))


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

    while key != 27:
        win.timeout(300)
        event = win.getch()
        if event == printable_num[len(printable_num)-1]:
            break
        elif event == printable_num[0]:
            screen.addstr("The User Pressed Lower Case p")
        #event = screen.getch()

        newNum()
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

popping()
"""
#cursor is hidden
curs_set(False) #nem műkszik

#Usually curses applications turn off automatic echoing of keys to the screen,
#in order to be able to read keys and only display them under certain circumstances.
curses.noecho()

#react to keys instantly, without requiring the Enter key to be pressed
curses.cbreak()

#Before doing anything, curses must be initialized. This is done by calling
#the initscr() function, which will determine the terminal type, send any
#required setup codes to the terminal, and create various internal
#data structures. If successful, initscr() returns a window object representing
#the entire screen; this is usually called screen after the name of the
#corresponding C variable.
screen = curses.initscr()

#window
begin_x = 0
begin_y = 0
height = 10
width = 30
win = curses.newwin(height, width, begin_y, begin_x)

#moves to a given y,x coordinate first before displaying the string
mvaddstr("3+2")

#it’s possible to not wait for the user using the nodelay() window method.
#getch() and getkey() for the window become non-blocking.
nodelay(True)

#refreshes the screen and then waits for the user to hit a key, displaying
#the key if echo() has been called earlier. You can optionally specify a
#coordinate to which the cursor should be moved before pausing.
#The getch() method returns an integer; if it’s between 0 and 255, it represents
#the ASCII code of the key pressed.
getch()





#curses.endwin()
"""
