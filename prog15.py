def bilinear_interpolation(x0, y0, x1, y1, q00, q10, q01, q11, x, y):
    """
    Bilinear interpolation function.

    Parameters:
    - x0, y0: Coordinates of the first point.
    - x1, y1: Coordinates of the second point.
    - q00, q10, q01, q11: Values at the four corners of the rectangle.
    - x, y: The coordinates where interpolation is needed.

    Returns:
    - The interpolated value.
    """
    if x0 == x1 or y0 == y1:
        # Handle the case where x0 is equal to x1 or y0 is equal to y1
        return q00 if x == x0 and y == y0 else None
    else:
        r1 = (x1 - x) / (x1 - x0) * q00 + (x - x0) / (x1 - x0) * q10
        r2 = (x1 - x) / (x1 - x0) * q01 + (x - x0) / (x1 - x0) * q11

        result = (y1 - y) / (y1 - y0) * r1 + (y - y0) / (y1 - y0) * r2

        return result

# Get values from the user
x0 = float(input("Enter the x-coordinate of the first point: "))
y0 = float(input("Enter the y-coordinate of the first point: "))
q00 = float(input("Enter the value at the first point: "))

x1 = float(input("Enter the x-coordinate of the second point: "))
y1 = float(input("Enter the y-coordinate of the second point: "))
q10 = float(input("Enter the value at the second point: "))

x01 = float(input("Enter the x-coordinate of the third point: "))
y01 = float(input("Enter the y-coordinate of the third point: "))
q01 = float(input("Enter the value at the third point: "))

x11 = float(input("Enter the x-coordinate of the fourth point: "))
y11 = float(input("Enter the y-coordinate of the fourth point: "))
q11 = float(input("Enter the value at the fourth point: "))

x_interpolate = float(input("Enter the x-coordinate where interpolation is needed: "))
y_interpolate = float(input("Enter the y-coordinate where interpolation is needed: "))

# Perform interpolation
result = bilinear_interpolation(x0, y0, x1, y1, q00, q10, q01, q11, x_interpolate, y_interpolate)

# Check if the result is not None before printing
if result is not None:
    print(f"The interpolated value at ({x_interpolate}, {y_interpolate}) is {result}")
else:
    print("Error: x0 is equal to x1 or y0 is equal to y1, division by zero.")
