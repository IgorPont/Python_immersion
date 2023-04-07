"""
Напишите функцию для транспонирования матрицы
"""


def transpose_matrix(matrix: list) -> list:
    """The function that transposes the matrix"""
    # Create an empty matrix the size of the original matrix
    trans_matrix: list = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]

    return trans_matrix


def print_matix(matrix: list) -> None:
    """Matrix output function in the console"""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f'{matrix[i][j]}', end=' ')
        print()
    print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matix(matrix)
print_matix(transpose_matrix(matrix))

# Test
# matrix = pymatrix.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# pymatrix_transpose = matrix.trans()
# print(matrix)
# print()
# print(pymatrix_transpose)
