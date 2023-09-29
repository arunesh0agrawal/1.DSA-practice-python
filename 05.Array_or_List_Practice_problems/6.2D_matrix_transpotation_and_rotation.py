# Problem statement : You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# Conditions: You have to rotate the image in-place, which means you have to modify the input 2D matrix directly
# Example : matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]


def rotate(matrix):

    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            # swapping elements (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix))
