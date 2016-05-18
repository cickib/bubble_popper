import curses
from curses import wrapper

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
#the entire screen; this is usually called stdscr after the name of the
#corresponding C variable.
stdscr = curses.initscr()

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
