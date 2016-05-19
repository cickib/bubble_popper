import curses
import time
import random
from curses import wrapper
import rocket

def main(screen):
    curses.noecho()
    curses.curs_set(0)
    begin_x = 0
    begin_y = 0
    height = 20
    width = 40
    win = curses.newwin(height, width, begin_y, begin_x)
    win.border(0)
    win.keypad(1)
    win.nodelay(1)
    title = "Bubble Popper"
    win.addstr(0, (width - len(title)) // 2, title) #nem műkszik
    win.refresh()


    printable_num = list(c for c in range(48, 58))
    printable_num.append(27)

    key = 48

    count = 0

    while key != 27:

        if count % 10 == 0 :
            x = random.randint(0, 2)
            num_y = 1
            num_x = random.randint(5, width-1)
            win.addstr(num_y, num_x, str(rocket.rockets[x][0]))
            win.addstr(num_y+1, num_x, str(rocket.rockets[x][1]))
            win.addstr(num_y+2, num_x, str(rocket.rockets[x][2]))
            while num_y != (height-3):
                win.clear()
                win.timeout(100)
                num_y += 1
                win.addstr(num_y, num_x, str(rocket.rockets[x][0]))
                win.addstr(num_y+1, num_x, str(rocket.rockets[x][1]))
                win.addstr(num_y+2, num_x, str(rocket.rockets[x][2]))
            #else:
            #    win.clear()

                """for y in range(1, 90):
                    win.refresh()
                    win.timeout(1000)
                    num_y += 1
                    win.addstr(num_y, num_x, str(rocket.rockets[x][0]))
                    win.addstr(num_y+1, num_x, str(rocket.rockets[x][1]))
                    win.addstr(num_y+2, num_x, str(rocket.rockets[x][2]))
                    y += 1""
            else:
                win.clear()"""
        #coord = [num_y, num_x)
        win.timeout(100)
        count += 1

        event = win.getch()
        if event == printable_num[len(printable_num)-1]:
            break

        if (event-48) == x:
            #curses.getsyx(num_y, num_x)
            #win.delch(num_y, num_x)
            win.clear()

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
curses.wrapper(main)
