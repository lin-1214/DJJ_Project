import numpy as np
import random

def first_order_diff(coeff, x, delta): 
    return (func_value(coeff, x + delta) - func_value(coeff, x)) / delta

def second_order_diff(coeff, x, delta):
    return (func_value(coeff, x + delta) - 2*func_value(coeff, x) + func_value(coeff, x - delta)) / delta**2

def func_value(coeff, x):
    return coeff[0] * x**2 + coeff[1] * x + coeff[2]

# generate a convex function f(x) = a1*x^2 + a2*x + a3
coeff = [random.randint(1, 50) for i in range(3)]
x = random.randint(-25, 25)
cur = func_value(coeff, x)
minimum = 0xFFFFFF
delta = 1e-3
lamb = 1
 
print(f"Convex function: {coeff[0]}x^2 + {coeff[1]}x + {coeff[2]}")

while(minimum > cur):
    minimum = cur
    x = x - lamb * first_order_diff(coeff, x, delta) / second_order_diff(coeff, x, delta)
    cur = func_value(coeff, x)

print(f"Minimim found at x = {x} by Newton method: {minimum}")