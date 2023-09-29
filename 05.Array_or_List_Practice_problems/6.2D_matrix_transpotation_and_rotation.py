# Problem statement : You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# Conditions: You have to rotate the image in-place, which means you have to modify the input 2D matrix directly
# Example : matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# method 1: (little pythonic)


def rotate_90_clockwise(matrix):  # [ T(n) : O(n2), S(n): O(1)]

    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            # Swapping elements (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix


# method 2: (Algorithmic way)


def rotate_90_clockwise_algo(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_90_clockwise_algo(matrix))
