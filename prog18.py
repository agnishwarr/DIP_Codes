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
original_matrix = generate_matrix()
print("Original Matrix:")
for row in original_matrix:
    print(' '.join(map(str, row)))
tx = int(input("Enter the x-translation value: "))
ty = int(input("Enter the y-translation value: "))
translated_matrix = generate_matrix(tx, ty)
print("\nTranslated Matrix:")
for row in translated_matrix:
    print(' '.join(map(str, row)))
