import numpy as np
import csv
import math

dataset = []
# a_1, a_2 ... a_L
params = np.array([])


with open('./dataset.csv', newline='') as csvfile:
  rows = csv.reader(csvfile)
  for row in rows:
    dataset.append(float(row[1]))

M = int(input("Please enter parameter M: "))
n_1, n_2, n_3, n_4 = 8, 38, 39, 41

LHS_Matr = []
RHS_Matr = []

for i in range(M+1):
  row = []
  for j in range(M+1):
    element = 0
    for n in range(n_1, n_2+1):
      element += math.pow(n, i + j)
    row.append(element)
  LHS_Matr.append(row)

for i in range(M+1):
  element = 0
  for n in range(n_1, n_2+1):
    element += dataset[n] * math.pow(n, i)
  RHS_Matr.append(element)

# print(f"shape: {np.shape(LHS_Matr)}")
INV_LHS_Matr = np.linalg.inv(LHS_Matr)
params = INV_LHS_Matr.dot(RHS_Matr)
print(f"params a: {params}") 

# calculate MSE
MSE = 0

for n in range(n_3, n_4+1):
  pred = 0
  for k in range(M+1):
    pred += params[k] * math.pow(n, k)
  print(f"prediction: {pred}, practical: {dataset[n]}")
  MSE += np.square(dataset[n] - pred)

MSE /= n_4 - n_3 + 1

# In case I, the best resilt occurs at M = 7
print(f"MSE for Aug: {MSE}")
  