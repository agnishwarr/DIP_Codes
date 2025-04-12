def generate_matrix():
    m_size = 10
    c_size = 3
    matrix = [[0] * m_size for i in range(m_size)]

    start = (m_size - c_size) // 2
    for i in range(start, start + c_size):
        for j in range(start, start + c_size):
            matrix[i][j] = 1
    return matrix
matrix = generate_matrix()
for row in matrix:
    print(' '.join(map(str, row)))
