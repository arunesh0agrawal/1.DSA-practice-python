# Merge Sort

## Merge Sort Algorithm
- Merge Sort is a divide-and-conquer algorithm that divides the array into smaller subarrays, sorts them, and then merges them back together in sorted order.

### Steps of Merge Sort Algorithm
- Divide: Recursively divide the array into two halves until each subarray has one element.
- Conquer: Sort and merge the subarrays to produce a sorted array.
- Combine: Merge the sorted subarrays to create a fully sorted array.

### Explanation of Example
Input Array: [64, 34, 25, 12, 22, 11, 90]

#### Steps:
Divide:

Split the array into halves: [64, 34, 25] and [12, 22, 11, 90].
Recursively divide these halves until each subarray contains one element.
Conquer (Merge):

Merge [64] and [34] → [34, 64].
Merge [34, 64] and [25] → [25, 34, 64].
Similarly, merge [12, 22] → [12, 22], then [12, 22] and [11] → [11, 12, 22], and finally [11, 12, 22] and [90] → [11, 12, 22, 90].
Combine:

Merge [25, 34, 64] and [11, 12, 22, 90] → [11, 12, 22, 25, 34, 64, 90].
Output: [11, 12, 22, 25, 34, 64, 90]

### Time Complexity
![image](https://github.com/user-attachments/assets/b41ae378-cd61-463e-b0f6-8546343a9d68)

### Advantages
- Stable Sorting: Maintains the relative order of equal elements.
- Guaranteed Performance: Always runs in 𝑂(𝑛log𝑛) regardless of input distribution.
- Divide and Conquer: Easy to parallelize.

### Disadvantages
- Space-Intensive: Requires additional memory for temporary arrays.
- Overhead for Small Arrays: Not as efficient for small datasets due to recursion overhead.

