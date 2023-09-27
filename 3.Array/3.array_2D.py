import numpy as np
import array

# method 1(bad way): Create a 2D array of integers using array module
two_d_array = array.array('i', [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Note:  Above raise a TypeError since a 2D array is not directly supported by the 'i' type code


# method 2( not really optimised way) : Define a nested list representing a 2D array
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flatten the nested list and create a 1D array
flat_list = [item for sublist in nested_list for item in sublist]

# Create a 1D array using the 'i' type code
two_d_array = array.array('i', flat_list)

print(two_d_array)  # [ output : array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])]


# method 3( best way): using numpy module


TwoDArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                     )  # [ T(n) : O(n), s(n): O(n)]
print(TwoDArray)  # [ output : [[1 2 3], [4 5 6], [7 8 9]]

# inserting elements
new2DArray = np.insert(TwoDArray, 0, [11, 12, 30], axis=0)
print(new2DArray)  # [output : [[11 12 30][ 1  2  3][ 4  5  6] [ 7  8  9]]
print(TwoDArray)

# method1:  accessing element
print(TwoDArray[0][1])
# method 2: accessing element


def access_element(arr, row_index, column_index):
    # learn here to loop through indices
    if row_index >= len(arr) or column_index >= len(arr):
        return "bad index"
    return arr[row_index][column_index]  # [output : T(n): O(1), S(n): O(1)]


print(access_element(TwoDArray, 2, 3))


# traversal 2D-array


def traversal_2d_array(arr):   # [ T(n): O(n2/MN), S(n) : O(1)]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j])


traversal_2d_array(TwoDArray)


# search 2D-array


def search_2d_array(arr, target):  # [T(n) : O(n2/mn), S(n): O(1) ]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == target:
                return True
    return False


print(search_2d_array(TwoDArray, 5))


# delete 2D array
# note: doesn't delete same array elements rather create new with remaining element
new2DArray = np.delete(TwoDArray, 0, axis=0)   # [ T(n) : O(mn), S(n): O(mn) ]
print(new2DArray)  # [ output : [[4 5 6] [7 8 9]] ]
