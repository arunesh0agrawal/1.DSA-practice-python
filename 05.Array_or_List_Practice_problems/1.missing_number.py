# problem statement : find missing number between in 1..100 in an array/list.

# build a array of natural number ( no need to do on coding platform)
natural_number = []


def fill_number(value):
    for i in range(value+1):
        natural_number.append(i)


fill_number(100)
natural_number.remove(55)


# method 1 ( brute force )  : using linear search


def missing_number_1(arr):  # [ t(n): O(n), S(n) : 1]
    for i in range(1, 101):
        if arr[i] != i:
            return i
    return "no missing number"


# method 2( mathematical way) : using natural number summation


def missing_number_2(arr, n):  # [ T(n): O(n), S(n): 1]
    sum_arr = sum(arr)
    sum_natural = n*(n+1)/2

    missing_val = int(sum_natural - sum_arr)

    return missing_val


print(missing_number_2(natural_number, 100))
