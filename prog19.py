def generate_matrix(cx=1, cy=1):
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
original_matrix = generate_matrix()
print("Original Matrix:")
for row in original_matrix:
    print(' '.join(map(str, row)))
cx = float(input("Enter the x-scaling factor: "))
cy = float(input("Enter the y-scaling factor: "))
scaled_matrix = generate_matrix(cx, cy)
print("\nScaled Matrix:")
for row in scaled_matrix:
    print(' '.join(map(str, row)))
