import numpy as np
from tqdm import tqdm

def gradient_descent(x, E, lamb = 1):
    for i in range(len(x)):
        x[i] -= lamb*E[i]
    return x

def Lalpha_norm(y, b, x, alpha=4):
    
    E = []
    for i in range(len(x)):
        tot = 0
        for j in range(len(y)):
            y_ = y[j] - b[0][j]*x[0] - b[1][j]*x[1] - b[2][j]*x[2]
            s = 0
            if (y_ > 0):
                s = 1
            elif (y_ < 0):
                s = -1
            tot -= b[i][j]*s*(abs(y_))**(alpha-1)

        E.append(alpha*tot)
    return E

y = [2, 3, 3, 4, 5, 4, 5]
b = [[1, 1, 1, 1, 1, 1, 1], 
     [1, 2, 3, 4, 5, 6, 7], 
     [1, -1, 1, -1, 1, -1, 1]]

x = [0, 0, 0]
iters = 100
lr = 2e-4

for i in tqdm(range(iters)):
    E = Lalpha_norm(y, b, x)
    x = gradient_descent(x, E, lamb = 0.8*(lr-lr/iters*i))

y_ = []
for i in range(len(y)):
    c = b[0][i]*x[0] + b[1][i]*x[1] + b[2][i]*x[2]
    y_.append(c)

print(f"New x found by Lnorm_alpha: {x}")
print(f"New y found by Lnorm alpha: {y_}")




