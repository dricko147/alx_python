def print_matrix_integer(matrix=[[]]):
    def print_matrix_with_indices(matrix):
    # Loop over each row
      for i in range(len(matrix)):
        # Loop over each column in the current row
        for j in range(len(matrix[i])):
            # Print element at row i, column j
            print(matrix[i][j], end=' ')
        # Print a new line after each row
        print()
 
 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Test the function with our matrix
print(matrix)
 