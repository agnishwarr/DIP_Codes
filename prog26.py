import numpy as np
def replicate_symmetric(matrix, padding):
    height, width = matrix.shape
    new_height = height + 2 * padding
    new_width = width + 2 * padding
    result_matrix = np.zeros((new_height, new_width))
    result_matrix[padding:padding + height, padding:padding + width] = matrix
    for x in range(padding):
        result_matrix[:, x] = result_matrix[:, 2 * padding - x - 1]
        result_matrix[:, new_width - x - 1] = result_matrix[:, new_width - 2 * padding + x]
    for y in range(padding):
        result_matrix[y, :] = result_matrix[2 * padding - y - 1, :]
        result_matrix[new_height - y - 1, :] = result_matrix[new_height - 2 * padding + y, :]
    return result_matrix
x = int(input("Enter the number of rows in the matrix: "))
y = int(input("Enter the number of columns in the matrix: "))
padding_width = int(input("Enter pad width: "))
matrix = np.random.randint(low=0, high=255, size=(x, y))
print("Original matrix:")
print(matrix)
result = replicate_symmetric(matrix, padding_width)
print("\nResult matrix:")
print(result)
