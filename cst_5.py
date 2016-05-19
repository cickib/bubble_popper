import curses
import time
import random
from curses import wrapper
import rocket

def main(screen):
    t_out = 250
    insane_mode = False
    key = 48
    score = 0
    life = 3
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
    title = "<< Bubble Popper >>"
    win.addstr(0, (width - len(title)) // 2, title)

    win.refresh()

    printable_num = list(c for c in range(48, 58))
    printable_num.append(27)

    life_heart = "💙 "
    life_lost = "💔 "

    #life_str = "Life:  " + str(life_heart*3)
    win.addstr(1, 5, "Life:  ")
    win.addstr(1, 12, life_heart)
    win.addstr(1, 14, life_heart)
    win.addstr(1, 16, life_heart)

    while key != 27:
        score_str = "Score: " + str(score)
        win.addstr(2, 5, score_str)
        if life == 2:
            win.addstr(1, 12, life_lost)
        if life == 1:
            win.addstr(1, 14, life_lost)
        if life == 0:
            win.addstr(1, 16, life_lost)
            win.clear()
            game_over = "Your score is " + str(score)
            win.addstr(15, 40, game_over)
            score_str = "Score: " + str(score)
            win.addstr(2, 5, score_str)
            break

        if score == 0:
            win.addstr(1, 45, "Press the right number for points.")
            win.addstr(2, 45, "If you miss one, you lost a life.")
        else:
            win.addstr(1, 45, (" "*34))
            win.addstr(2, 45, (" "*33))
        if t_out < 51:
            insane_mode = True
            win.addstr(1, 45, ("Insade mode: ON"))
        if score % 10 == 0:
            t_out -=50
        #if score == 20:
        #    exit()
        win.refresh()

        if count % 10 == 0 :
            x = random.randint(0, 9)
            num_y = 3
            num_x = random.randint(10, width-6)
            win.addstr(num_y, num_x, str(rocket.rockets[x][0]))
            win.addstr(num_y+1, num_x, str(rocket.rockets[x][1]))
            win.addstr(num_y+2, num_x, str(rocket.rockets[x][2]))
            while num_y != (height-4) or ((event-48) == x):
                win.refresh()
                win.timeout(t_out)
                num_y += 1
                win.addstr(num_y-1, num_x, "     ")
                win.addstr(num_y, num_x, str(rocket.rockets[x][0]))
                win.addstr(num_y+1, num_x, str(rocket.rockets[x][1]))
                win.addstr(num_y+2, num_x, str(rocket.rockets[x][2]))
                event = win.getch()
                if event == printable_num[len(printable_num)-1]:
                    exit()
                if (event-48) == x:
                    if insane_mode == False:
                        score += 1
                    else:
                        score += 5
                    win.addstr(num_y, num_x, "     ")
                    win.addstr(num_y+1, num_x, "     ")
                    win.addstr(num_y+2, num_x, "     ")
                    break

                win.addstr(num_y, num_x, "     ")
                win.addstr(num_y+1, num_x, "     ")
                win.addstr(num_y+2, num_x, "     ")
            else:
                life -= 1
            continue
        win.timeout(t_out)
        count += 1


curses.wrapper(main)
