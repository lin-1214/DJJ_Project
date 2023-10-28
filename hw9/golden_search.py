import numpy as np
import random

def diff(coeff, x): 
    return 2 * coeff[0] * x + coeff[1]

def func_value(coeff, x):
    return coeff[0] * x**2 + coeff[1] * x + coeff[2]

def golden_search(x_0, x_1, threshold, coeff):

    e = (-1 + np.sqrt(5)) / 2
    x_2 = x_0 + (x_1 - x_0) / (1 + e)
    while(abs(x_1 - x_0) >= threshold):
        x_3 = x_0 + (x_2 - x_0) / (1 + e)
        if (func_value(coeff, x_2) < func_value(coeff, x_3)):
            x_0 = x_1
            x_1 = x_3
        elif(func_value(coeff, x_2) > func_value(coeff, x_3)):
            x_1 = x_2
            x_2 = x_3
    
    return x_0, x_1

x_0 = random.randint(-25, 25)
x_1 = random.randint(50, 100)
threshold = 1e-5

# generate a convex function f(x) = a1*x^2 + a2*x + a3
coeff = [random.randint(1, 50) for i in range(3)]
while(diff(coeff, x_0) >= 0 or diff(coeff, x_1) <= 0):
    x_0 = random.randint(-25, 25)
    x_1 = random.randint(50, 100)
    
print(f"Convex function: {coeff[0]}x^2 + {coeff[1]}x + {coeff[2]}")

# apply golden search
x_0, x_1 = golden_search(x_0, x_1, threshold, coeff)
print(f"Points found by golden search, x_0: {x_0}, x_1: {x_1}")
print(f"Minimum value: {min(func_value(coeff, x_0), func_value(coeff, x_1))}")