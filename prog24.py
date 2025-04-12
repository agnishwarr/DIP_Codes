import numpy as np
def padding(matrix, pad_width):
    height, rows = matrix.shape
    new_height = height + 2 * pad_width
    new_width = rows + 2 * pad_width
    result_matrix = np.zeros((new_height, new_width), dtype=matrix.dtype)
    result_matrix[pad_width:new_height - pad_width, pad_width:new_width - pad_width] = matrix
    print(pad_width)
    print(new_height - pad_width)
    print(new_width - pad_width)
    return result_matrix
x = int(input("Enter the number of rows in the matrix: "))
y = int(input("Enter the number of columns in the matrix: "))
pad = int(input("Enter pad width: "))
matrix = np.random.randint(low=0, high=255, size=(x, y))
print("Original matrix: ")
print(matrix)
result = padding(matrix, pad)
print("\nResult matrix: ")
print(result)
