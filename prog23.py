import numpy as np
def boundary_pixel(matrix, y, x):
    neighbours = []
    rows, columns = matrix.shape

    if x == 0 or y == 0 or x == rows - 1 or y == columns - 1:
        return True
    else:
        return False
def padding(matrix):
    height, rows = matrix.shape
    result_matrix = np.zeros((rows+2,height+2))
    for y in range(height+1):
        for x in range(rows+1):
            if(boundary_pixel(result_matrix,y,x)):
                result_matrix[y,x]=0
            else:
                result_matrix[y,x] = matrix[y-1][x-1]
    return result_matrix
x = int(input("enter the no of rows in the matrix: "))
y= int(input("enter the no of columns in the matrix: "))
matrix = np.random.randint(low=0, high=255, size=(x, y))
print("original matrix: ")
print(matrix)
result = padding(matrix)
print("\nResult matrix: ")
print(result)
