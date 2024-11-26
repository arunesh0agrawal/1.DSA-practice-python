# selection sort

## Algorithm
- Traverse the list from the beginning.
- For each element, assume it is the minimum.
- Compare it with the rest of the unsorted elements to find the actual minimum.
- Swap the found minimum element with the current element.
- Repeat for all elements.

## Explanation of Example
Input: [64, 25, 12, 22, 11]

###Steps:

- Find the smallest element (11), swap with the first element: [11, 25, 12, 22, 64]
- Find the smallest element in the remaining array (12), swap with the second element: [11, 12, 25, 22, 64]
- Find the smallest element in the remaining array (22), swap with the third element: [11, 12, 22, 25, 64]
- The array is now sorted.
Output: [11, 12, 22, 25, 64]

## Time Complexity

- Best Case: 𝑂(𝑛2)
- Worst Case: 𝑂(𝑛2)
- Average Case: 𝑂(𝑛2)
  
## Space Complexity
- Auxiliary Space: 𝑂(1)
O(1) (Selection sort is an in-place algorithm.)

## Advantages
- Simple to understand and implement.
- Does not require additional memory for sorting.

## Disadvantages
- Inefficient for large datasets due to 𝑂(𝑛2) complexity.
- Number of comparisons is fixed and does not adapt based on input data.
