def insertion_sort(arr):
    # Traverse from the second element to the last
    for i in range(1, len(arr)):
        # Store the current element to be inserted
        current = arr[i]
        j = i - 1
        # Shift elements of the sorted portion to the right if they are greater
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert the current element into its correct position
        arr[j + 1] = current
    return arr

# Example usage
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = insertion_sort(array)
print("Sorted array:", sorted_array)
