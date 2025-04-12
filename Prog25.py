import numpy as np
def padding_symmetric(matrix):
    height, width = matrix.shape
    result_matrix = np.zeros((height+2,width+2))
    for y in range(height+2):
        for x in range(width+2):
            if height+1>y>0 and x<1:  #left most border
                result_matrix[y,x] = matrix[y-1,x]
            elif width+1>x>0 and y<1: #top most border
                result_matrix[y,x] = matrix[y,x-1]
            elif x>width and 0<y<height+1: #right most border
                result_matrix[y,x] = matrix[y-1,x-2]
            elif y>height and 0<x<width+1: #bottom most border
                result_matrix[y,x] = matrix[y-2,x-1]
            result_matrix[1:width+1,1:height+1] = matrix
    return result_matrix
x = int(input("enter the no of rows in the matrix: "))
y= int(input("enter the no of columns in the matrix: "))
matrix = np.random.randint(low=0, high=255, size=(x, y))
print("original matrix: ")
print(matrix)
result = padding_symmetric(matrix)
print("\nResult matrix: ")
print(result)
