import numpy as np
import random
import matplotlib.pyplot as plt

# construct dataset
pts = int(input("Enter the number of data point: "))
dataset = [(random.randint(-10, 10), random.randint(-10, 10)) for i in range(pts)]
print(f"Data Points: {dataset}")

# calculate SVD target, matrix A
avg_pt = np.sum([dataset[i][0] for i in range(pts)])/pts, np.sum([dataset[i][1] for i in range(pts)])/pts
A = [(dataset[i][0] - avg_pt[0], dataset[i][1] - avg_pt[1]) for i in range(pts)]
print(f"Adjusted matrix A: {A}")

# apply SVD
U, S, Vh = np.linalg.svd(A, full_matrices=True)
print(f"SVD results: U: {U}, S: {S}, Vh:{Vh}")
V = np.transpose(Vh)

fig, ax = plt.subplots()
ax.axline((avg_pt[0] + V[0][0], avg_pt[1] + V[0][1]), (avg_pt[0] - V[0][0], avg_pt[1] - V[0][1]), color='C8', label='regression line')
ax.set_title("PCA prediction result")
for i in range(pts):
    plt.plot(dataset[i][0], dataset[i][1], "ro")

ax.legend()

