# Quick Sort

 - Quick Sort is a divide-and-conquer algorithm used to sort an array or list. It works by selecting a "pivot" element, partitioning the array around the pivot, and recursively sorting the partitions.

## How Quick Sort Works
1. Choose a Pivot:
Select an element as the "pivot." This can be:
The first element.
The last element.
A random element.
The median element (rarely used for simplicity).

2. Partition the Array:
Rearrange the array so that:
All elements smaller than the pivot come before it.
All elements larger than the pivot come after it.
The pivot ends up in its correct sorted position.

3. Recursively Sort:
Apply the same process to the subarrays to the left and right of the pivot.

## Step-by-Step Example
```
Input:
arr = [3, 6, 8, 10, 1, 2, 1]

Choose Pivot: pivot = 1 (last element).

Partition:
Smaller: [1] (values ≤ pivot).
Greater: [3, 6, 8, 10, 2] (values > pivot).
Result: [1] + [1] + quick_sort([3, 6, 8, 10, 2])
Recurse on [3, 6, 8, 10, 2]:

Pivot = 2.
Partition:
Smaller: [] (no values ≤ pivot).
Greater: [3, 6, 8, 10] (values > pivot).
Result: [] + [2] + quick_sort([3, 6, 8, 10])
Recurse on [3, 6, 8, 10]:

Pivot = 10.
Partition:
Smaller: [3, 6, 8].
Greater: [].
Result: quick_sort([3, 6, 8]) + [10] + [].
Continue until fully sorted:

[3, 6, 8] → [3] + [6] + [8].
Final Result:
[1, 1, 2, 3, 6, 8, 10]
```

## Time Complexity

![image](https://github.com/user-attachments/assets/4c16fc03-dd05-4e05-a5af-43e2adcbc0da)

## Advantages
- Very efficient on average for large datasets.
- In-place (can be implemented to use minimal extra memory).

## Disadvantages
- Performance can degrade to 𝑂(𝑛2) if the pivot is poorly chosen.
- Not stable (relative order of equal elements may not be preserved).



