import numpy as np

def get_neighbors(matrix, x, y):
    neighbors = []
    rows, columns = matrix.shape

    # Horizontal and vertical neighbors
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

    # Diagonal neighbors
    if x > 0 and y > 0:
        northwest = (x - 1, y - 1)
        neighbors.append(northwest)

    if x > 0 and y < columns - 1:
        northeast = (x - 1, y + 1)
        neighbors.append(northeast)

    if x < rows - 1 and y > 0:
        southwest = (x + 1, y - 1)
        neighbors.append(southwest)

    if x < rows - 1 and y < columns - 1:
        southeast = (x + 1, y + 1)
        neighbors.append(southeast)

    return neighbors

# Get matrix dimensions from the user
rows = int(input("Enter the number of rows in the matrix: "))
columns = int(input("Enter the number of columns in the matrix: "))

# Create a matrix with random values
matrix = np.random.randint(1, 100, size=(rows, columns))
print(matrix)

# Get the coordinates from the user
x = int(input("Enter the x coordinate of the point: "))
y = int(input("Enter the y coordinate of the point: "))

# Check if the coordinates are within the matrix bounds
if 0 <= x < rows and 0 <= y < columns:
    # Get the neighbors and print their values along with locations
    neighbors = get_neighbors(matrix, x, y)

    print(f"Original point at ({x}, {y}) has value: {matrix[x, y]}")

    for neighbor in neighbors:
        nx, ny = neighbor
        print(f"Neighbor at ({nx}, {ny}) has value: {matrix[nx, ny]}")
else:
    print("Invalid coordinates. Point is outside the matrix bounds.")
