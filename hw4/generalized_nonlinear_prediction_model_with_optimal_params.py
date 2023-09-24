import numpy as np
import csv
import math

dataset = []
# a_1, a_2 ... a_L, b_1, b_2, ... b_L-1
params = np.array([])


with open('./dataset.csv', newline='') as csvfile:
  rows = csv.reader(csvfile)
  for row in rows:
    dataset.append(float(row[1]))

# maximum L=20
L = int(input("Choose param L: "))
alpha = float(input("Choose param alpha: "))
# n_1 >= max(range(L))+2
n_1, n_2, n_3, n_4 = 8, 38, 39 , 41
w_n = []
for i in range(n_2 - n_1 + 1):
  if (i<10):
    w_n.append(0.5)
  elif (i<15):
    w_n.append(0.7)
  elif(i<20):
    w_n.append(1)
  elif (i<25):
    w_n.append(1.2)
  elif(i<30):
    w_n.append(1.5)
  elif(i<31):
    w_n.append(5)

print(f"n_1, n_2, n_3, n_4 = {n_1}, {n_2}, {n_3}, {n_4}")
print(f"L: {L}")
print(f"sum of w_n: {np.sum(w_n)}")

dataset=np.array(dataset)

LHS_Matr = []
RHS_Matr = []


for i in range(L):
  row = []
  for j in range(L):
    element = 0
    for n in range(n_1, n_2+1):
      element += dataset[n-i-1] * dataset[n-j-1]
      # element[1] += dataset[n-i-1] * (dataset[n-j-1] - dataset[n-j-2])**2
      # s for b goes to only L-1
      # if (n-j-2 < 0):
      #   element[1] = 0
      element *= w_n[n - n_1]
    row.append(element)
  for j in range(L):
    element = 0 
    for n in range(n_1, n_2+1):
      element += dataset[n-i-1] * math.pow((dataset[n-j-1] - dataset[n-j-2]), alpha)
      element *= w_n[n - n_1]
    row.append(element)
  LHS_Matr.append(row)

for i in range(L):
  row = []
  for j in range(L):
    element = 0
    for n in range(n_1, n_2+1):
      element += math.pow((dataset[n-i-1] - dataset[n-i-2]), alpha) * dataset[n-j-1]
      element *= w_n[n - n_1]
      # s for b goes to only L-1
    row.append(element)
  for j in range(L):
    element = 0
    for n in range(n_1, n_2+1):
      element += math.pow((dataset[n-i-1] - dataset[n-i-2]), alpha) * math.pow((dataset[n-j-1] - dataset[n-j-2]), alpha)
      element *= w_n[n - n_1]
    row.append(element)
  LHS_Matr.append(row)

for i in range(L):
  element = 0
  for n in range(n_1, n_2+1):
    element += dataset[n-i-1] * dataset[n]
    element *= w_n[n - n_1]
  RHS_Matr.append(element)

for i in range(L):
  element = 0
  for n in range(n_1, n_2+1):
    element += math.pow((dataset[n-i-1] - dataset[n-i-2]), alpha) * dataset[n]
    element *= w_n[n - n_1]
  RHS_Matr.append(element)

LHS_Matr = np.array(LHS_Matr)
RHS_Matr = np.array(RHS_Matr)

inv_LHS_Matr = np.linalg.inv(LHS_Matr)
params = inv_LHS_Matr.dot(RHS_Matr)

# print(f"{LHS_Matr}, {RHS_Matr}")
print(f"params: {params}")

MSE = 0
for n in range(n_3, n_4+1):
  pred = 0
  for i in range(L):
    pred += params[i] * dataset[n-i-1]
  for i in range(L-1):
    pred += params[i+L] * (dataset[n-i-1] - dataset[n-i-2])**alpha
  print(f"prediction: {pred}, practical: {dataset[n]}")
  MSE += np.square(dataset[n] - pred)

MSE /= n_4 - n_3 + 1
print(f"MSE for Aug: {MSE}")

filename = "results.csv"

# writing to csv file 
with open(filename, 'a') as csvfile:

    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the data rows 
    csvwriter.writerow([f"{L}", f"{alpha}", f"{str(MSE)}"])