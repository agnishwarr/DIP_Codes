import numpy as np
m1 = np.zeros((10, 10))
dm = np.zeros((5, 5))
for i in range(5):
    for j in range(5):
        dm[i, j] = np.mean(m1[2*i:2*(i+1), 2*j:2*(j+1)])
print("Original Matrix:")
print(m1)
print("\nDownscaled Matrix:")
print(dm)
