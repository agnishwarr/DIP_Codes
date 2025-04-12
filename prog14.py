import numpy as np
def horizontal_interpolation(x0, x1, q0, q1, x):
    if x0 == x1:
        return q0 if x == x0 else None
    else:
        return q0 + (q1 - q0) * (x - x0) / (x1 - x0)
x0 = float(input("Enter the x-coordinate of the first point: "))
q0 = float(input("Enter the value at the first point: "))
x1 = float(input("Enter the x-coordinate of the second point: "))
q1 = float(input("Enter the value at the second point: "))
x_interpolate = float(input("Enter the x-coordinate where interpolation is needed: "))
result = horizontal_interpolation(x0, x1, q0, q1, x_interpolate)
if x0 == x1:
    print("Error: x0 is equal to x1, division by zero.")
else:
    print("Original Matrix:")
    print(f"x0: {x0}, q0: {q0}")
    print(f"x1: {x1}, q1: {q1}")
    print("\nInterpolated Value:")
    print(f"Interpolated at x={x_interpolate}: {result}")
