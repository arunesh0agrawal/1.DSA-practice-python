## binary search on 1D array

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Target not found
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Example usage
arr = [1, 3, 5, 7, 9, 11]
target = 7
print(binary_search_recursive(arr, target, 0, len(arr) - 1))  # Output: 3
