import numpy as np
angle = np.radians(float(input("Enter an angle: ")))
def generate_matrix(angle):
    rotational_angle = angle
    matrix_size = 10
    central_size = 3
    matrix = np.zeros((matrix_size, matrix_size), dtype=int)
    start = (matrix_size - central_size) // 2
    for i in range(start, start + central_size):
        for j in range(start, start + central_size):
            new_cord = rotation(i, j, rotational_angle)
            matrix[int(new_cord[0, 0]), int(new_cord[1, 0])] = 1
    return matrix
def rotation(x, y, angle):
    transformation_matrix = np.array([[np.cos(angle), np.sin(angle), 0],
                                      [-np.sin(angle), np.cos(angle), 0],
                                      [0, 0, 1]])
    coordinates = np.matmul(transformation_matrix, [[x], [y], [1]])
    return coordinates
original_matrix = generate_matrix(0)  
print("Original Matrix:")
for row in original_matrix:
    print(' '.join(map(str, row)))
rotated_matrix = generate_matrix(angle)
print("\nRotated Matrix:")
for row in rotated_matrix:
    print(' '.join(map(str, row)))
