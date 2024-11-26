def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Number of passes
        swapped = False  # Keep track of whether any elements were swapped
        for j in range(n - 1 - i):  # Traverse the unsorted part
            if arr[j] > arr[j + 1]:
                # Swap if the current element is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps were made, the array is sorted
        if not swapped:
            break
    return arr

# Example usage
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(array)
print("Sorted array:", sorted_array)
