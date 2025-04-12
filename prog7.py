import numpy as np
matrix_10x10 = np.zeros((10, 10))
print("Original 10x10 Matrix:")
print(matrix_10x10)
matrix_5x5 = matrix_10x10[::2, ::2]
print("\nReduced 5x5 Matrix:")
print(matrix_5x5)
