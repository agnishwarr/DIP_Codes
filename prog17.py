import numpy as np
def translate_matrix(matrix, dx, dy, selected_row, selected_col):
    rows, cols = matrix.shape
    translated_matrix = np.zeros_like(matrix, dtype=np.int64)
    for i in range(rows):
        for j in range(cols):
            ni, nj = i - dy, j - dx 
            if 0 <= ni < rows and 0 <= nj < cols:
                translated_matrix[i, j] = matrix[ni, nj]
    return translated_matrix
def main():
    # Get the matrix size from the user
    rows = int(input("Enter the number of rows in the matrix: "))
    cols = int(input("Enter the number of columns in the matrix: "))
    original_matrix = np.zeros((rows, cols), dtype=np.int64)
    selected_row = int(input("Enter the row index of the selected location: "))
    selected_col = int(input("Enter the column index of the selected location: "))
    original_matrix[selected_row, selected_col] = 1 
    dx = int(input("Enter the horizontal translation factor: "))
    dy = int(input("Enter the vertical translation factor: "))
    translated_matrix = translate_matrix(original_matrix, dx, dy, selected_row, selected_col)
    print("\nOriginal Matrix:")
    print(original_matrix)
    print("\nTranslated Matrix:")
    print(translated_matrix)
if __name__ == "__main__":
    main()
