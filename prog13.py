import numpy as np
def vertical_interpolation(y0, y1, q0, q1, y):
    if y0 == y1:
        return q0 if y == y0 else None
    else:
        return q0 + (q1 - q0) * (y - y0) / (y1 - y0)
y0 = float(input("Enter the y-coordinate of the first point: "))
q0 = float(input("Enter the value at the first point: "))
y1 = float(input("Enter the y-coordinate of the second point: "))
q1 = float(input("Enter the value at the second point: "))
y_interpolate = float(input("Enter the y-coordinate where interpolation is needed: "))
Y = np.array([[y0], [y1]])
Q = np.array([[q0], [q1]])
Y_interpolate = np.array([[y_interpolate]])
result = q0 + (q1 - q0) * (Y_interpolate - y0) / (y1 - y0)
if y0 == y1:
    print("Error: y0 is equal to y1, division by zero.")
else:
    print("Original Matrix:")
    print(f"y0: {y0}, q0: {q0}")
    print(f"y1: {y1}, q1: {q1}")
    print("\nInterpolated Value:")
    print(f"Interpolated at y={y_interpolate}: {result.item()}")
