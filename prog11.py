import numpy as np
def get_neighbors(matrix, x, y):
    neighbors = []
    rows, columns = matrix.shape
    if x > 0:
        north = (x - 1, y)
        neighbors.append(north)
    if y > 0:
        west = (x, y - 1)
        neighbors.append(west)
    if x < rows - 1:
        south = (x + 1, y)
        neighbors.append(south)
    if y < columns - 1:
        east = (x, y + 1)
        neighbors.append(east)
    return neighbors
rows = int(input("Enter the number of rows in the matrix: "))
columns = int(input("Enter the number of columns in the matrix: "))
matrix = np.random.randint(1, 100, size=(rows, columns))
print(matrix)
x = int(input("Enter the x coordinate of the point: "))
y = int(input("Enter the y coordinate of the point: "))
if 0 <= x < rows and 0 <= y < columns:
    neighbors = get_neighbors(matrix, x, y)
    print(f"Original point at ({x}, {y}) has value: {matrix[x, y]}")
    for neighbor in neighbors:
        nx, ny = neighbor
        print(f"Neighbor at ({nx}, {ny}) has value: {matrix[nx, ny]}")
else:
    print("Invalid coordinates. Point is outside the matrix bounds.")
