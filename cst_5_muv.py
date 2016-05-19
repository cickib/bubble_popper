import curses
import time
import random
from curses import wrapper
import rocket
import rocket_ops



def main(screen):
    ops = ["+", "-"]
    muv = []
    key = 48
    score = 0
    count = 0
    curses.noecho()
    curses.curs_set(0)
    begin_x = 0
    begin_y = 0
    height = 30
    width = 80
    win = curses.newwin(height, width, begin_y, begin_x)
    # win.refresh()
    win.keypad(1)
    win.border(0)
    win.nodelay(1)
    title = "Bubble Popper"
    win.addstr(0, (width - len(title)) // 2, title) #nem műkszik
    score_str = "Score: " + str(score)
    win.addstr(1, 5, score_str)
    win.refresh()

    printable_num = list(c for c in range(48, 58))
    printable_num.append(27)

    while key != 27:

        score_str = "Score: " + str(score)
        win.addstr(1, 5, score_str)
        if score == 5:
            exit()
        win.refresh()

        if count % 10 == 0 :
            num_y = 2
            num_x = random.randint(10, width-6)
            num_1 = random.randint(0, 9)
            num_2 = random.randint(0, 9)

            rocket_op = [num_1, ops[random.randint(0,1)], num_2]
            for o in range(0, (len(rocket_op))):
                muv.append(rocket_op[o])
            muvs = (rocket_ops.muv[0], rocket_ops.muv[1], rocket_ops.muv[2])
            win.addstr(num_y, num_x, str(rocket_ops.muv[0]))
            win.addstr(num_y, num_x+1, str(rocket_ops.muv[1]))
            win.addstr(num_y, num_x+2, str(rocket_ops.muv[2]))
            while num_y != (height-4) or ((event-48) == muvs):
                #win.clear()
                win.refresh()
                win.timeout(100)
                num_y += 1
                win.addstr(num_y-1, num_x, "     ")
                win.addstr(num_y, num_x, str(rocket_ops.muv[0]))
                win.addstr(num_y, num_x+1, str(rocket_ops.muv[1]))
                win.addstr(num_y, num_x+2, str(rocket_ops.muv[2]))
                event = win.getch()
                if event == printable_num[len(printable_num)-1]:
                    exit()
                if (event-48) == muvs:
                    score += 1
                    win.addstr(num_y, num_x, "     ")
                    win.addstr(num_y, num_x+1, "     ")
                    win.addstr(num_y, num_x+2, "     ")
                    break
                win.addstr(num_y, num_x, "     ")
                win.addstr(num_y, num_x+1, "     ")
                win.addstr(num_y, num_x+2, "     ")
            continue

        win.timeout(100)
        count += 1



   #if event ==
    # #        snake = [[4,10]]
    # #        title = ' Hello snake! '
    # #        win.addstr(0, (curses.COLS - len(title)) // 2, title)
    #

curses.wrapper(main)
