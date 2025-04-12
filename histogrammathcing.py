import numpy as np
import matplotlib.pyplot as plt
def nk(matrix):
    max_val = 8
    d = {}
    for i in range(max_val):
        d[i] = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            d[matrix[i][j]] += 1
    return d
def pr(matrix, d):
    total_pixels = matrix.shape[0] * matrix.shape[1]
    max_val = 8
    for i in range(max_val):
        d[i] = d[i] / total_pixels
    return d
def sk(l, d, j):
    summation = sum([d[i] for i in range(j + 1)])
    return round((l - 1) * summation)
matrix = np.random.randint(low=0, high=8, size=(64, 64))
nk_original = nk(matrix)
pr_original = pr(matrix, nk_original)
zq_updated = {0: 0, 1: 0, 2: 0, 3: 0.15, 4: 0.20, 5: 0.30, 6: 0.20, 7: 0.15}
rk = {}
for i in range(8):
    rk[i] = [sk(8, pr_original, i), sk(8, zq_updated, i)]
def plot_histogram(distributions, titles):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(distributions[0].keys(), distributions[0].values(), color='blue')
    plt.title(titles[0])
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Probability')
    plt.subplot(1, 2, 2)
    plt.bar(distributions[1].keys(), distributions[1].values(), color='green')
    plt.title(titles[1])
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Probability')
    plt.tight_layout()
    plt.show()
plot_histogram([pr_original, zq_updated], ['Original Probability Distribution', 'Updated Probability Distribution'])
