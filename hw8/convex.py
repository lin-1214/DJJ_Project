import numpy as np
import random
from tqdm import tqdm

def calc_util(i, j, k, coefficients):
    ans = 0
    for m in range(len(coefficients)):
        for n in range(len(coefficients[m])-1, -1, -1):
            if m == 0: 
                ans += pow(i, n) * coefficients[m][2-n]
            elif m == 1:
                ans += pow(j, n) * coefficients[m][2-n]
            elif m == 2:
                ans += pow(k, n) * coefficients[m][2-n]
    return ans

def convex(a, b, vec_len, coefficients):
    lhs = 0
    rhs = 0
    c = random.randint(1, int(np.floor(vec_len/2)))
    print(f"c: {c}")
    lhs = calc_util(a[0], a[1], a[2], coefficients) + c * (calc_util(b[0], b[1], b[2], coefficients) \
                                                           - calc_util(a[0], a[1], a[2], coefficients)) / vec_len
    new_point = tuple([a[0] + c * (b[0] - a[0]), a[1] + c * (b[1] - a[1]), a[2] + c * (b[2] - a[2])] / vec_len)
    rhs = calc_util(new_point[0], new_point[1], new_point[2], coefficients)  

    print(f"lhs = {lhs}, rhs = {rhs}")
    if (lhs >= rhs):
        return True
    else:
        return False
    
def step_search(pt1, pt2, partition, i, coefficients):
    prt = np.linspace(int(pt1[i]), int(pt2[i]), partition)
    delta = prt[1] - prt[0]

    smallest = calc_util(pt1[0], pt1[1], pt1[2], coefficients)
    point = pt1[i]
    for pt in prt:
        if (i==0):
            tmp = calc_util(pt, pt1[1], pt1[2], coefficients)
            if tmp <= smallest:
                smallest = tmp
                point = pt
        elif (i==1):
            tmp = calc_util(pt1[0], pt, pt1[2], coefficients)
            if tmp <= smallest:
                smallest = tmp
                point = pt
        elif (i==2):
            tmp = calc_util(pt1[0], pt1[0], pt, coefficients)
            if tmp <= smallest:
                smallest = tmp
                point = pt
    
    return point
    
# step1: generate target function u(x_1, x_2, ... x_n)
# Assume utility function u(x_1, x_2, ... x_n) = (a1 * x_1^2 + a2 * x_2^2 + ...) + 
# (b1 * x_1 + b2 * x_2 ...) + (c1 + c2 ...)

# function u(x_1, x_2, ... x_n) = x_1^2 + 2x_1 - 3 + x_2^2 + 4x_2 + 3 + x_3^2 - 6x_3 +9

n = 3 # 3-dimension
# [[a1, b1, c1], [a2, b2, c2] ...]
coefficients = [[20 - random.randint(1, 40) for j in range(3)] for i in range(n)]

points = []
for i in tqdm(range(-40, 40)) :
    for j in range(-40, 40):
        for k in range(-40, 40):
            if(calc_util(i, j, k, coefficients)%3 == 0) :
                points.append(tuple([i, j, k]))

print("Done finding points!")

point_a = tuple([])
point_b = tuple([])
while(point_a == point_b):
    point_a = points[random.randint(0, len(points))]
    point_b = points[random.randint(0, len(points))]

print(f"A{point_a}, B{point_b}")

# step2: check whether it is a convex function
tmp = 0
for i in range(3):
    tmp += pow(point_a[i]-point_b[i], 2)

vector_len = np.sqrt(tmp)

flag = True
if (convex(point_a, point_b, vector_len, coefficients)):
    print("FuncT10n U 1s A c0Nv3x fUnct1on \(^_^)/")
else :
    flag = False
    print("FuncT10n U 1s not A c0Nv3x fUnct1on QQ")

# step3: step search method to minimize function u
optimal_x = 0
optimal_y = 0
optimal_z = 0

if (flag):
    for i in range(n):
        partition = step_search(point_a, point_b, 100, i, coefficients)
        if (i==0):
            optimal_x = partition
        elif (i==1):
            optimal_y = partition
        elif (i==2):
            optimal_z = partition

    print(f"minimum point: ({optimal_x}, {optimal_y}, {optimal_z})")
else:
    print("Please generate the convex function again 13(>_O)13")