# hetrogenous,  ordered and mutable

# defining a empty list
demo_list = []

# define a list with element
my_list = [1, 2, 3, "hi", 6]  # [T(n): O(n), S(n) : O(n)]
print(my_list)  # [output : [1, 2, 3, 'hi', 6]]

# accessing a list
print(my_list[1])  # [output : 2, T(n): O(1), S(n) : 1]

# index of list
print(my_list.index("hi"))  # [ index(value), output: 3 ]

# count occurenace of value
print(my_list.count(3))  # [ count(value), output: 1 ]

# Traversing a list : method 1
for i in my_list:
    print(i)  # [ T(n): O(n), S(n) : 1]
# Traversing a list : method 2
for i in range(len(my_list)):  # [ T(n): O(n), S(n) : 1]
    print("index", i, "has value", my_list[i])
# Traversing a list : method 3
for i, j in enumerate(my_list):  # [ T(n): O(n), S(n) : 1]
    print(i, j)  # i = index, j = value

# searching operation


def search_value(new_list, target):
    for i in my_list:
        if i == target:
            return "present"
    return "not present"


print(search_value(my_list, 5))


# all add operations

# append a list
my_list.append("bye")  # [append(value),  T(n) : O(1), S(n) : O(1)]
print(my_list)  # [output : [1, 2, 3, 'hi', 6, 'bye']]

# insert a list
my_list.insert(0, "hello")  # [ insert(index, value), T(n) : O(n), S(n) : O(1)]
print(my_list)  # [output : ['hello', 1, 2, 3, 'hi', 6, 'bye'] ]

# update a list
my_list[2] = "updated"  # [ T(n) : O(1), S(n) : O(1)]
print(my_list)  # [ output : ['hello', 1, 'updated', 3, 'hi', 6, 'bye']]

# extend a list
new_list = [4, 6]
my_list.extend(new_list)  # [ extend(list), T(n) : O(n), S(n) : O(n)]
print(my_list)  # [ output : ['hello', 1, 'updated', 3, 'hi', 6, 'bye', 4, 6]]

# all subtracting operations

# slciing a list
print(my_list[0:2])  # [ output: ['hello', 1]]
my_list[0:2] = ["N1", "N2"]
print(my_list)  # [output : ['N1', 'N2', 'updated', 3, 'hi', 6, 'bye', 4, 6] ]
# [ [start, last, step], output: ['N1', 'updated', 'hi', 'bye', 6]]
print(my_list[::2])


# pop value
pop_value = my_list.pop()
print(pop_value)  # [output: removes last value]
pop_value = my_list.pop(4)  # [ pop(index), T(n): O(n), S(n): O(1)]
print(pop_value)  # [ output : pop value of index 4 ]

# remove
my_list.remove('bye')  # [ remove(value), T(n): O(n), S(n) : 1]
print(my_list)  # [ output: output : ['N1', 'N2', 'updated', 3, 6, 4]]

# delete
del my_list[1]  # [output : removes value of index 1 ]
del my_list[1: 3]  # [ output: removes a list of value]


# all mathematical operations

# + operation
a = [1, 2, 3]
b = [4, 5]
print(a+b)  # [ output: [1, 2, 3, 4, 5]]

# * operator ( multiply operator)
# [ ouptut : [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3] ]
print(my_list*6)

# len/sum/min/max
print(len(my_list))
print(sum(a))
print(max(a))
print(min(a))

# sort/sorted
a.sort()  # [ output: inplace sorting]
c = sorted(a, reverse=True)  # [ output: outplace sorting, return new list]
print(c)

# from string to list
my_str = "spam"
print(list(my_str))  # [ output : ['s', 'p', 'a', 'm'] ]
my_str = "spam spam spam"
new_list = my_str.split()  # [ split(sep), output : ['spam', 'spam', 'spam']]
print(new_list)

# (from list to string )or (string to formatted string)
print("-".join(my_str))  # [ output : s-p-a-m- -s-p-a-m- -s-p-a-m]
# note: list should be homogenous
print("-".join(['1', '2', '3']))   # [ "delimiter".join(list), output : 1-2-3 ]
