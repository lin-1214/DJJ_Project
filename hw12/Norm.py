import numpy as np
import random

def L_Norm(y, A):
    A_trans = np.transpose(A)
    C_inv = np.linalg.inv(np.matmul(A_trans, A))
    z = np.transpose(A)
    return np.matmul(np.matmul(C_inv, z), y)

# m, n = 9, 5
m, n = 7, 3

# y = [random.randint(1, 25) for i in range(m)]
# b = [[random.randint(-5, 5) for j in range(m)] for i in range(n)]

y = [2, 3, 3, 4, 5, 4, 5]
b = [[1, 1, 1, 1, 1, 1, 1],
     [1, 2, 3, 4, 5, 6, 7],
     [1, -1, 1, -1, 1, -1, 1]]

print(f"vector y: {y}")
print(f"vector bs: {b}")

A = np.transpose(b)
x = L_Norm(y, A)
print(f"x: {x}")

y_ = []
for i in range(m):
    tot = 0
    for j in range(n):
        tot += b[j][i] * x[j]
    y_.append(tot)

print(f"vector y by L_Norm: {y_}")