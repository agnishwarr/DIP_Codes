import numpy as np

# Create two matrices (arrays of 0s and 1s)
m1 = np.array([[1, 0], [1, 1]])
m2 = np.array([[0, 1], [1, 0]])

#  AND
a = np.logical_and(m1, m2)
print("Logical AND:")
print(a)

#  OR
b = np.logical_or(m1, m2)
print("\nLogical OR:")
print(b)

# NOT
c = np.logical_not(m1)
print("\nLogical NOT:")
print(c)

# XOR
d = np.logical_xor(m1, m2)
print("\nLogical XOR:")
print(d)

# NAND
e = np.logical_not(np.logical_and(m1, m2))
print("Logical NAND:")
print(e)

# NOR
f = np.logical_not(np.logical_or(m1, m2))
print("\nLogical NOR:")
print(f)

# XNOR
g = np.logical_not(np.logical_xor(m1, m2))
print("\nLogical XNOR:")
print(g)
