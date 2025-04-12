import numpy as np
original_matrix = np.zeros((5, 5), dtype=int)
upscaled_matrix = np.kron(original_matrix, np.ones((2, 2), dtype=int))
print("Original 5x5 matrix of zeros:")
print(original_matrix)
print("\nUpscaled 10x10 matrix of zeros:")
print(upscaled_matrix)
