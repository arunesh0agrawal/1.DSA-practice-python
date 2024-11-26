def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Assume the current index is the smallest
        min_index = i
        
        # Find the smallest element in the unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage
array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(array)
print("Sorted array:", sorted_array)
