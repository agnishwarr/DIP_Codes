import numpy as np
def print_menu():
    print("\nMatrix Operations Menu:")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Scalar Multiplication")
    print("5. Scalar Division")
    print("6. Scalar Addition")
    print("7. Scalar Subtraction")
    print("8. Exit")
def add_matrices(A, B):
    return np.add(A, B)
def subtract_matrices(A, B):
    return np.subtract(A, B)
def multiply_matrices(A, B):
    return np.matmul(A, B)
def scalar_multiplication(scalar, A):
    return scalar * A
def scalar_division(scalar, A):
    return A / scalar
def scalar_addition(scalar, A):
    return A + scalar
def scalar_subtraction(scalar, A):
    return A - scalar
A = np.array([[1, 2, 3], [3, 4, 5], [1, 1, 1]])
B = np.array([[1, 2, 3], [3, 4, 5], [1, 1, 1]])
while True:
    print_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        print("Added Matrix:")
        print(add_matrices(A, B))
    elif choice == '2':
        print("Subtracted Matrix:")
        print(subtract_matrices(A, B))
    elif choice == '3':
        print("Multiplied Matrix:")
        print(multiply_matrices(A, B))
    elif choice == '4':
        scalar = float(input("Enter scalar value: "))
        print("Scalar Multiplication:")
        print(scalar_multiplication(scalar, A))
        print(scalar_multiplication(scalar, B))
    elif choice == '5':
        scalar = float(input("Enter scalar value: "))
        print("Scalar Division:")
        print(scalar_division(scalar, A))
        print(scalar_division(scalar, B))
    elif choice == '6':
        scalar = float(input("Enter scalar value: "))
        print("Scalar Addition:")
        print(scalar_addition(scalar, A))
        print(scalar_addition(scalar, B))
    elif choice == '7':
        scalar = float(input("Enter scalar value: "))
        print("Scalar Subtraction:")
        print(scalar_subtraction(scalar, A))
        print(scalar_subtraction(scalar, B))
    elif choice == '8':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
