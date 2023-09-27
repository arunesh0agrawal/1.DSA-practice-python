# Two ways to define array
# 1. import array ( built-in) [ implemented in array_1D.py file]
# 2. import np ( np:numpy need installation)

# use-case: 1D optimised array and 2D array i python

# defining how 1D-array are implemented using numpy module

import numpy as np

# defining empty 1D-array using numpy module
# note: no memory is being allocated, only object
my_arr = np.array([], dtype='i')  # [ T(n): O(1), s(n): O(1) creation]
print(my_arr)  # [ output: [] ]

# 1D-array with elements
my_arr1 = np.array([1, 2, 3, 4])
print(my_arr1)  # [ output: [1, 2,3, 4], T(n): O(n), S(n): O(n)]

# Note : more you can read about numpy on offical site.
