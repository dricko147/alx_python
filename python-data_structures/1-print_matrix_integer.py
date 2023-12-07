def print_matrix_integer(matrix=[[]]):
    def print_matrix_integer(matrix=[[]]):
     for i in matrix:
        for j, num in enumerate(i):
            if j == len(i) - 1:
                print("{:d}".format(num), end="")
            else:
                print("{:d} ".format(num), end="")
                
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Test the function with our matrix
print(matrix)
 