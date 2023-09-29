# Implementing list compreshion
# works for [ list, range, string, tuple]
# use-case :
# 1. in place of for loop
# 2. lesser code

# basic list comprehension
my_list = [10, 8, 2, 7, 8, 8]
new_list = [item+2 for item in my_list]
print(new_list)

# multiple loop list comprehension
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(pairs)

# nested loop
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# syntax : [ [expression == inner_loop] for i in iterable ]
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)

# if conditional statement
new_list = [x for x in my_list if x % 2 == 0]
print(new_list)

# if-else condition
new_list = [x+2 if x % 2 == 0 else x+1 for x in my_list]
print(new_list)

# function calling list comprehension


def cube(x):
    return x**3


numbers = [1, 2, 3, 4, 5]
cubes = [cube(x) for x in numbers]
print(cubes)
