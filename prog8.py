import numpy as np
matrix = np.array([[0, 1, 1], [0, 1, 0], [0, 0, 1]])
x1 = int(input("enter x coordinate of p"))
y1 = int(input("enter y coordinate of p"))
x2 = int(input("enter x coordinate of q"))
y2 = int(input("enter y coordinate of q"))
q =(x2,y2)
def neighbour(matrix, x, y):
    neighbours = []
    rows, column = matrix.shape
    if x > 0:
        north = (x - 1, y)
        neighbours.append(north)
    if y > 0:
        south = (x, y - 1)
        neighbours.append(south)
    if x < rows - 1:
        east = (x + 1, y)
        neighbours.append(east)
    if y < column - 1:
        west = (x, y + 1)
        neighbours.append(west)
    return neighbours
a = matrix[x1, y1]
b = matrix[x2, y2]
list = neighbour(matrix,x1,y1)
if a==b:
    if q in list:
        print("given two coordinates are 4 connected")
    else:
        print("not 4 connected")
else:
    print("not 4 connected")
