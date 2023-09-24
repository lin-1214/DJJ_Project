import numpy as np
import csv

dataset = []
# a_1, a_2 ... a_L
params = np.array([])

with open('./dataset.csv', newline='') as csvfile:
  rows = csv.reader(csvfile)
  for row in rows:
    dataset.append(float(row[1]))

# n_1, n_2, n_3, n_4
L = int(input("Choose param L: "))
n_1, n_2, n_3, n_4 = 5, 14, 15, 20

print(f"n_1, n_2, n_3, n_4 = {n_1}, {n_2}, {n_3}, {n_4}")
print(f"L: {L}")

dataset=np.array(dataset)

LHS_Matr = []
RHS_Matr = []

 
for j in range(L):
    row = []
    for k in range(L):
        element = 0
        for n in range(n_1, n_2):
            element += dataset[n-j-1] * dataset[n-k-1]
        row.append(element)
    LHS_Matr.append(row)

for j in range(L):
    element = 0
    for n in range(n_1, n_2):
        element += dataset[n-j-1] * dataset[n]
    RHS_Matr.append(element)

# print(f"shape for LHS matr: {np.shape(LHS_Matr)}")
# print(f"shape for RHS matr: {np.shape(RHS_Matr)}")

LHS_Matr = np.array(LHS_Matr)
RHS_Matr = np.array(RHS_Matr)
RHS_Matr.reshape((len(RHS_Matr), 1))

Inv_LHS_Matr = np.linalg.inv(LHS_Matr)
params = Inv_LHS_Matr.dot(RHS_Matr)
print(f"Params: {params}")

# calculate MSE
MSE = 0
for n in range(n_3, n_4):
   pred = 0
   for i in range(L):
      pred += params[i] * dataset[n-i-1]
   print(f"Prediction: {pred}, Practical: {dataset[n]}")
   MSE += np.square(dataset[n] - pred)

print(f"MSE for July: {MSE}")
