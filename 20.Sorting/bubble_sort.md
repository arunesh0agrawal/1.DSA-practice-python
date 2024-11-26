# Bubble Sort Algorithm
//Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

## Steps of Bubble Sort Algorithm
- Start at the beginning of the list. 
- Compare each pair of adjacent elements:
- If the current element is greater than the next, swap them.
- At the end of each pass through the list, the largest element "bubbles up" to its correct position.
- Reduce the range of unsorted elements and repeat the process.
- Stop when no swaps are needed in a complete pass, meaning the list is sorted.


## Explanation of Example
Input Array: [64, 34, 25, 12, 22, 11, 90]

### Steps:

#### Pass 1: Compare each pair and swap if needed:

[64, 34] → Swap → [34, 64]
[64, 25] → Swap → [34, 25, 64]
[64, 12] → Swap → [34, 25, 12, 64]
[64, 22] → Swap → [34, 25, 12, 22, 64]
[64, 11] → Swap → [34, 25, 12, 22, 11, 64]
[64, 90] → No Swap → [34, 25, 12, 22, 11, 64, 90]
Largest element 90 is now in its correct position.

#### Pass 2: Repeat for the unsorted part [34, 25, 12, 22, 11]:

Result: [25, 12, 22, 11, 34, 64, 90]
#### Pass 3: Repeat for the unsorted part [25, 12, 22, 11]:

Result: [12, 11, 22, 25, 34, 64, 90]

#### Pass 4: Repeat for the unsorted part [12, 11]:

Result: [11, 12, 22, 25, 34, 64, 90]
Output: [11, 12, 22, 25, 34, 64, 90]

### Time Complexity
#### Best Case: 
𝑂(𝑛)
O(n) when the array is already sorted (optimized version with the swapped flag).
#### Worst Case: 
𝑂(𝑛2)
O(n2) when the array is sorted in reverse order.
#### Average Case: 
𝑂(𝑛2)
  
### Space Complexity
Auxiliary Space: 
𝑂(1)
O(1) as Bubble Sort is an in-place sorting algorithm.

## Advantages
Simple and easy to understand.
No additional memory is required (in-place sorting).
## Disadvantages
Inefficient for large datasets due to 𝑂(𝑛2) complexity.
Comparisons are always made, even if the list is already sorted (unless optimized).
