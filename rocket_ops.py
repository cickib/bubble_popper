import random
import curses
num_1 = random.randint(0, 9)
num_2 = random.randint(0, 9)
ops = ["+", "-"]
muv = []
rocket_op = [num_1, ops[random.randint(0,1)], num_2]
for o in range(0, (len(rocket_op))):
    muv.append(rocket_op[o])
