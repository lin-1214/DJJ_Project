import numpy as np
import random
from tqdm import tqdm

def partial_diff(x, y, coeff, dir):
    if (dir == 0):
        # x direction
        return 2*coeff[dir][0]*x + coeff[dir][1]*x
    elif (dir == 1):
        # y direction
        return 2*coeff[dir][0]*y + coeff[dir][1]*y
    else:
        print("Out of dimension")
        return

def func_value(x, y, coeff):
    ans = 0
    # print(f"{int(x*10)/10}, {int(y*10)/10}")
    for i in range(2):
        for j in range(3):
            if (i == 0):
                ans += coeff[i][j] * (int(x*10)/10)**(2-j)
            else:
                ans += coeff[i][j] * (int(y*10)/10)**2-j
    return ans 

def grad(x, y, coeff, threshold, round, lr):
    a1 = partial_diff(x,y,coeff,0)
    a2 = partial_diff(x,y,coeff,1)
    if (round % 20 == 0):
        print(f"Current learning rate: {lr}")
        print(f"a1, a2: {a1}, {a2}")

    if ( abs(a1) < threshold and abs(a2) < threshold ):
        # print(f"Final a1, a2: {a1}, {a2}") 
        return x, y
    else:
        smallest = 0xffffff
        c = 0
        for i in (range(-30000, 30000)):
            if (func_value(x + lr*a1/100, y + lr*a2/100, coeff) < smallest):
                smallest = func_value(x + lr*a1/100, y + lr*a2/100, coeff)
                c = i

        # print(f"Current (x, y): {x + c*a1}, {y + c*a2}")
        round += 1
        if (round == 80):
            lr /= 3
            round = 0

        x, y = grad(x + lr*a1/100, y + lr*a2/100, coeff, threshold, round, lr)
        return x, y


# f(x,y) = ax^2 + bx + c + dy^2 + ey + f
coeff = [[-random.randint(1,20) for j in range(3)] for i in range(2)]
threshold = 800
x_init, y_init = 25, 75
print(f"Function f: {coeff[0][0]}x^2 + {coeff[1][0]}y^2 + {coeff[0][1]}x + {coeff[1][1]}y + {coeff[0][2]+coeff[1][2]}")

round = 0
lr = 3e-2
x_final, y_final = grad(x_init, y_init, coeff, threshold, round, lr)

print(f"Optimal (x,y) s.t. f(x,y) has minimum: {x_final}, {y_final}")
print(f"Minimum value: {func_value(x_final, y_final, coeff)}")