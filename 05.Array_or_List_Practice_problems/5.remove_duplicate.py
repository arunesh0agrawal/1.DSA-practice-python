# problem statement : write a function to remove the duplicate numbers on given interger array/list.
# exampple : [15, 23, 4, 5, 35, 15, 4]
# output : [15, 23, 4, 5, 35]

# method 1 (pythonic) : set()


def remove_duplicate_1(arr):
    unique_list = set(arr)  # [ T(n) : O(n), S(n) : O(n)]
    return unique_list     # but it returns set here not list


# method 2(optimized) : algorithmic


def remove_duplicate(arr):
    # [ note: use of set make searching O(1) due to hash table implementation]
    unique_list = set()
    result = []  # [optional : only if we want to return list on set]
    for i in arr:  # [ T(n) : O(n), S(n) ]
        if i in unique_list:
            continue
        unique_list.add(i)
        result.append(i)
    return result


print(remove_duplicate([15, 23, 4, 5, 35, 15, 4]))
