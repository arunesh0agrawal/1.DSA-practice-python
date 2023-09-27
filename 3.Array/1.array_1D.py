# Two ways to define array
# 1. import array ( built-in)
# 2. import np ( np:numpy need installation)

# defining how 1D-array are implemented using array module

import array

# defining empty array
# [t(n): O(1), s(n): holds a reference to a memeory block]
my_arr = array.array('i')
print(my_arr)  # output: array('i')

# defining array with elememts
my_arr1 = array.array('i', [1, 2, 3, 4])  # [t(n): O(n), S(n): O(n)]
print(my_arr1)  # output : array('i', [1, 2, 3, 4])

# appeneding array
my_arr1.append(8)  # [t(n) : O(n), S(n) : O(1) ]
print(my_arr1)  # [output : array('i', [1, 2, 3, 4, 8])]

# insertion to array
my_arr1.insert(0, 6)  # [insert(index, value), t(n) : O(n), s(n): O(1)]
print(my_arr1)  # output : array('i', [6, 1, 2, 3, 4])

# traversal of an array


def traverse_array(arr):  # [ t(n) : O(n), S(n): O(1)]
    for i in arr:
        print(i)


traverse_array(my_arr1)

# accessing array elemet
print(my_arr1[2])  # [output : 2, t(n): 1, s(n): 1]

# serching array element


def liner_search(arr, target):  # [ t(n): O(n), s(n): O(1) ]
    for i in arr:
        if i == target:
            return "found"
    return "not found"


element = liner_search(my_arr1, 8)
print(element)  # [ output : not found]

# delete an element
# [remove(value) = first occurenace only,  t(n): O(n), s(n): O(1)]
my_arr1.remove(6)
print(my_arr1)  # [output : array('i', [1, 2, 3, 4])]

# pop element
val = my_arr1.pop()  # [t(n): O(1), s(n): O(1)]
print(val)  # [output : 8]
val = my_arr1.pop(3)  # [ pop(index), t(n): O(n), s(n): O(1)]
print(val)  # [output : 4]

# find index
print(my_arr1.index(2))  # [index(value), output : 1, t(n): O(1), s(n): O(1)]

# slice element
print(my_arr1[1:3])

# reverse array
my_arr1.reverse()
print(my_arr1)  # [output: array('i', [8, 4, 3, 2, 1])]

# extend a list
my_arr2 = array.array('i', [3,  8, 9])
my_arr1.extend(my_arr2)  # [ t(n): O(n+m), s(n): O(n+m)]
print(my_arr1)  # [ output : array('i', [3, 2, 1, 7, 8, 9]) ]

# count occurance
print(my_arr1.count(3))  # [count(value), output : 2 ]

# get buffer info
# [ output : (2620058733296[address of buffer], 6[size of buffer])]
print(my_arr1.buffer_info())

# add item from list to array
my_list = [10, 11, 12]
my_arr1.fromlist(my_list)
print(my_arr1)  # output : array('i', [3, 2, 1, 3, 8, 9, 10, 11, 12])

# convert to list
print(my_arr1.tolist())  # return another list
print(my_arr1)  # array stays same
