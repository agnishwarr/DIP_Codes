import numpy as np
matrix = np.random.randint(0, 256, size=(10, 10))
threshold = 127
output = (matrix >= threshold) * 1
print("Original Matrix:")
print(matrix)
print("\nOutput with threshold:")
print(output)
