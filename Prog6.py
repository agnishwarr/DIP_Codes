import numpy as np
def neighbors(matrix, x, y):
    neighbors = []
    rows, columns = matrix.shape
    for i in range(max(0, x - 1), min(rows, x + 2)):
        for j in range(max(0, y - 1), min(columns, y + 2)):
            if (i, j) != (x, y):
                neighbors.append((i, j))
    return neighbors
def m_connected(matrix, p, q):
    p_neighbors = neighbors(matrix, *p)
    q_neighbors = neighbors(matrix, *q)
    common_neighbors = set(p_neighbors) & set(q_neighbors)
    for neighbor in common_neighbors:
        if matrix[neighbor[0], neighbor[1]] == 1:
            return False
    return True
matrix = np.array([[0, 1, 1], [0, 1, 0], [0, 0, 1]])
x1 = int(input("Enter x coordinate of P: "))
y1 = int(input("Enter y coordinate of P: "))
x2 = int(input("Enter x coordinate of Q: "))
y2 = int(input("Enter y coordinate of Q: "))
p = (x1, y1)
q = (x2, y2)
if matrix[p[0], p[1]] != matrix[q[0], q[1]]:
    print("P and Q are not M-connected.")
else:
    if m_connected(matrix, p, q):
        print("P and Q are M-connected.")
    else:
        print("P and Q are not M-connected.")
