# inplace algorithm( main use)
def quick_sort_inplace(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort the subarrays
        quick_sort_inplace(arr, low, pivot_index - 1)  # Left subarray
        quick_sort_inplace(arr, pivot_index + 1, high)  # Right subarray

def partition(arr, low, high):
    # Choose the pivot (we'll use the last element)
    pivot = arr[high]
    i = low - 1  # Pointer for the smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    
    # Swap the pivot element with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
quick_sort_inplace(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 1, 2, 3, 6, 8, 10]




# outplace algorithm
# def quick_sort(arr):
#     # Base case: Arrays with 0 or 1 element are already sorted
#     if len(arr) <= 1:
#         return arr
    
#     # Choose the pivot (we'll use the last element here)
#     pivot = arr[-1]
    
#     # Partition the array into two subarrays
#     smaller, greater = [], []
#     for num in arr[:-1]:  # Exclude the pivot
#         if num <= pivot:
#             smaller.append(num)
#         else:
#             greater.append(num)
    
#     # Recursively sort the subarrays and combine them
#     return quick_sort(smaller) + [pivot] + quick_sort(greater)

# # Example usage
# arr = [3, 6, 8, 10, 1, 2, 1]
# sorted_arr = quick_sort(arr)
# print(sorted_arr)  # Output: [1, 1, 2, 3, 6, 8, 10]
