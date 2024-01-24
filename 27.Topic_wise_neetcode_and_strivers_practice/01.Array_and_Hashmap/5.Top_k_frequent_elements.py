# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 
# Releated Pronlems : 
# 1)  Word frequency
# 2) Kth largest elemnet in an array 
# 3) sort characters by frequency

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

import heapq
from collections import Counter

def top_k_frequent(nums, k):  [ # T(n) : O(nlogn)]
    # Use Counter to get the frequency of each element
    frequency_counter = Counter(nums)

    # Use a min heap to keep track of the k most frequent elements
    heap = []
    
    for num, freq in frequency_counter.items():
        # Push the elements onto the heap with their frequencies as the key
        heapq.heappush(heap, (freq, num))
        
        # If the heap size exceeds k, pop the smallest element
        if len(heap) > k: # this step helping us to make t(n): O (nlogk), otherwise it could be O(nlogn)
            heapq.heappop(heap)

    # Extract the elements from the heap (they are stored in reverse order)
    result = [item[1] for item in heap][::-1]
    
    return result

# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
result = top_k_frequent(nums, k)
print(result)




