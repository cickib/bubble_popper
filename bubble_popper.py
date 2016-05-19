#Bubble Popper by Péter Szladovits & Bella Kocsis - very basic version
#If the right number is pressed, the bubble pops, score is added.
# After every 10 points, the player levels up, which speeds up the bubbles.
# On the 5th level, insade mode gives 5x more points for 1 bubble popped.
# If the bubble reaches the bottom without being popped, player losts 1 life.
# If esc pressed or player lost all lives, the game exits.

import curses
import time
import random
from curses import wrapper
import bubbles

#main function, it does the whole thing
def main(screen ):
#initializing the window
    curses.noecho()
    curses.curs_set(0)
    begin_x = 0
    begin_y = 0
    height = 30
    width = 80
    win = curses.newwin(height, width, begin_y, begin_x)
    win.keypad(1)
    win.border(0)
    win.nodelay(1)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    win.bkgd(' ', curses.color_pair(1))
    title = "⊰⊰  Bubble Popper ⊱⊱"
    win.addstr(0, (width - len(title)) // 2, title)
    divide = "_"*(width-2)
    win.addstr(3, 1, divide)
    win.refresh()
#initializing the starting values of the game
    insane_mode = False
    key = 48
    count = 0
#possible player inputs
    printable_num = list(c for c in range(48, 58))
    printable_num.append(27)
#initializing life
    life = 3
    life_heart = "💙 "
    life_lost = "💔 "
    win.addstr(1, 5, "Life:  ")
    win.addstr(1, 12, life_heart)
    win.addstr(1, 14, life_heart)
    win.addstr(1, 16, life_heart)
#initializing score
    score = 0
    score_str = "Score: " + str(score)
    win.addstr(2, 5, score_str)
#initializing levels and speed
    level = 1
    t_out = 250
#the game continues until the player has at least 1 life and doesn't press esc
    while key != 27 and life > 0:
        level_str = "Level " + str(level)
        win.addstr(2, 12, str(score))
#adding the lost hearts
        if life == 2:
            win.addstr(1, 12, life_lost)
        elif life == 1:
            win.addstr(1, 14, life_lost)
        elif life == 0:
            break
#giving instructions to the player
        if score == 0:
            win.addstr(1, 43, "Press the right number for points.")
            win.addstr(2, 43, "If you miss one, you lost a life.")
        elif score == 1:
            win.addstr(1, 43, (" "*35))
            win.addstr(2, 43, (" "*35))
            win.addstr(1, 43, "It gets faster by leveling up.")
        else:
            win.addstr(1, 43, (" "*36))
            win.addstr(2, 43, (" "*35))
            win.addstr(1, 70, level_str)
#setting the current level and speed
        if score >1 and score % 10 == 0:
            level += 1
            t_out -=50
        if t_out < 51:
            insane_mode = True
            win.addstr(2, 62, ("Insane mode: ON"))
        win.refresh()
#generating a random bubble, importing it from bubbles
        if count % 10 == 0 :
            x = random.randint(0, 9)
            num_y = 4
            num_x = random.randint(10, width-6)
            win.addstr(num_y, num_x, str(bubbles.bubble[x][0]))
            win.addstr(num_y+1, num_x, str(bubbles.bubble[x][1]))
            win.addstr(num_y+2, num_x, str(bubbles.bubble[x][2]))
#making the bubble move downwards
            while num_y != (height-4) or ((event-48) == x):
                win.refresh()
                win.timeout(t_out)
                num_y += 1
                win.addstr(num_y-1, num_x, "     ")
                win.addstr(num_y, num_x, str(bubbles.bubble[x][0]))
                win.addstr(num_y+1, num_x, str(bubbles.bubble[x][1]))
                win.addstr(num_y+2, num_x, str(bubbles.bubble[x][2]))
                event = win.getch()
#handling the esc button
                if event == printable_num[len(printable_num)-1]:
                    exit()
#handling when the player presses the right button
                if (event-48) == x:
                    if insane_mode == False:
                        score += 1
                    else:
                        score += 5
                    win.addstr(num_y, num_x, "     ")
                    win.addstr(num_y+1, num_x, "     ")
                    win.addstr(num_y+2, num_x, "     ")
                    break
#if the bubble reaches the bottom of the window, it "pops" = deleted
                win.addstr(num_y, num_x, "     ")
                win.addstr(num_y+1, num_x, "     ")
                win.addstr(num_y+2, num_x, "     ")
#strange construct, couldn't make it work otherwise
            else:
                life -= 1
            continue
        win.timeout(t_out)
        count += 1

#the game is called
curses.wrapper(main)
