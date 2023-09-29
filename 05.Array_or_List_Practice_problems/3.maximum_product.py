# problem statement : find maximun product of two intergers.
# sub-problem : find two maximum integers.

# exaample : [1, 7, 3, 4, 9, 5]
# output :  63

# method 1 : pythonic way
def max_product_1(arr):
    arr.sort(reverse=True)  # [ T(n) : O(nlogn), S(n) : O(1)]
    return arr[0]*arr[1]


# method 2: algorithmic way

def max_product_2(arr):
    max1, max2 = 0, 0
    for num in arr:  # [ T(n) : O(n), s(n): O(1) ]
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return max2*max1


numbers = [1, 7, 3, 4, 9, 5]
print(max_product_2(numbers))
