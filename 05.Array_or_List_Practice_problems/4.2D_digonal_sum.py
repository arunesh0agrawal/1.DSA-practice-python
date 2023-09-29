# problem statement: calcu;ate the sum of diagonal elements.

# example: [[1,2,3], [4, 5, 6], [7, 8, 9]]
# ouptut : 15

def diagonal_sum(arr):  # [ T(n): O(n), S(n): O(1)]
    sum = 0
    for i in range(len(arr[0])):
        sum += arr[i][i]
    return sum


print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
