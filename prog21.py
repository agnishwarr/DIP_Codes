import numpy as np
def generate_matrix(tx=0, ty=0):
    m_size = 10
    c_size = 3
    matrix = [[0] * m_size for _ in range(m_size)]
    start = (m_size - c_size) // 2
    for i in range(start, start + c_size):
        for j in range(start, start + c_size):
            new_i = i + tx
            new_j = j + ty

            if 0 <= new_i < m_size and 0 <= new_j < m_size:
                matrix[new_i][new_j] = 1
    return matrix
def generate_scaled_matrix(cx=1, cy=1):
    m_size = 10
    c_size = 3
    matrix = [[0] * m_size for _ in range(m_size)]

    start = (m_size - c_size) // 2
    for i in range(start, start + c_size):
        for j in range(start, start + c_size):
            new_i = int(i * cx)
            new_j = int(j * cy)

            if 0 <= new_i < m_size and 0 <= new_j < m_size:
                matrix[new_i][new_j] = 1
    return matrix
def generate_rotated_matrix(angle):
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
while True:
    print("\nMenu:")
    print("1. Translate Matrix")
    print("2. Scale Matrix")
    print("3. Rotate Matrix")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        tx = int(input("Enter the x-translation value: "))
        ty = int(input("Enter the y-translation value: "))
        translated_matrix = generate_matrix(tx, ty)
        print("\nTranslated Matrix:")
        for row in translated_matrix:
            print(' '.join(map(str, row)))
    elif choice == 2:
        cx = float(input("Enter the x-scaling factor: "))
        cy = float(input("Enter the y-scaling factor: "))
        scaled_matrix = generate_scaled_matrix(cx, cy)
        print("\nScaled Matrix:")
        for row in scaled_matrix:
            print(' '.join(map(str, row)))
    elif choice == 3:
        angle = np.radians(float(input("Enter an angle in degrees: ")))
        rotated_matrix = generate_rotated_matrix(angle)
        print("\nRotated Matrix:")
        for row in rotated_matrix:
            print(' '.join(map(str, row)))
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
