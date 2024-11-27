# Insertion Sort

## Steps of Insertion Sort Algorithm
- Start with the second element (index 1), as the first element is trivially sorted.
- Compare the current element with the elements in the sorted portion of the array (to its left).
- Shift elements in the sorted portion to the right to make space if the current element is smaller.
- Insert the current element into its correct position.
- Repeat the process for all elements.

## Explanation of Example
Input Array: [64, 34, 25, 12, 22, 11, 90]

### Steps:
Start with the second element (34):

Compare with 64 → Insert 34 before 64.
Result: [34, 64, 25, 12, 22, 11, 90]
Take the next element (25):

Compare with 64 → Shift 64.
Compare with 34 → Insert 25 before 34.
Result: [25, 34, 64, 12, 22, 11, 90]
Take the next element (12):

Compare with 64 → Shift 64.
Compare with 34 → Shift 34.
Compare with 25 → Shift 25.
Insert 12 at the beginning.
Result: [12, 25, 34, 64, 22, 11, 90]
Take the next element (22):

Compare with 64 → Shift 64.
Compare with 34 → Shift 34.
Compare with 25 → Shift 25.
Insert 22 after 12.
Result: [12, 22, 25, 34, 64, 11, 90]
Continue this process for 11 and 90.

Output: [11, 12, 22, 25, 34, 64, 90]

## Time Complexity
- Best Case: 𝑂(𝑛)
- O(n) when the array is already sorted (only one comparison per element).

- Worst Case: 𝑂(𝑛2)
O(n2) when the array is sorted in reverse order.

- Average Case: 𝑂(𝑛2)

## Space Complexity
- Auxiliary Space: 𝑂(1)
- O(1), as it is an in-place sorting algorithm.

## Advantages
- Simple and easy to implement.
- Efficient for small or nearly sorted datasets.

## Disadvantages
- Inefficient for large datasets due to 𝑂(𝑛2) complexity.
- Requires multiple data movements for each element.
