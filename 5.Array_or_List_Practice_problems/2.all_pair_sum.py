# problem statement : write a program to find all pairs of intergers whos some is equal to given number.
# condition : same elements are not allowed
# given :  an array of n intergers.
# target : m

# example -> [2, 7, 11, 15]
# output ->  [0,1]

# QUESTIONS you should ask interviwer to make it intractive and clear
# 1.does array contains any negative number.
# 2. what if pair repeats, should i print it
# 3. if reverse of pair is acceptable
# 4. do we need to print distinct pair only , like not (3,3)
# 5. how big an array

# method 1( brute force) : nested loop


def pair_sum_1(arr, target):  # [ T(n) : O (n2), S(n): O(1)]
    seen = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            # condition[optional] : when you are asking for distinct values
            if arr[i] == arr[j]:
                continue
            # condition[optional] : without both reciprocal/symmetric/inverse pairs
            if (arr[i], arr[j]) in seen or (arr[j], arr[i]) in seen:
                continue
            elif arr[i]+arr[j] == target:
                seen.append((arr[i], arr[j]))
                print((i, j))


# method 2( optimized ) : finding compliments

def pair_sum_2(arr, target):  # T(n) : O(nm), m<<<n
    seen = []

    for i in arr:
        compliment = target - i
        if compliment == i:
            continue
        elif compliment in seen:  # to print all reciprocal also add condition: or i in seen.
            print(compliment, i)
        else:
            seen.append(i)


pair_sum_2([5, 7, 3, 4, 11, 4,  8, 1, 5, 2, 15], 8)


#
