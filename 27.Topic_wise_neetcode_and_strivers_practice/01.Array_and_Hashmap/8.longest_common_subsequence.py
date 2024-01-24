# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# # related problems
# 1.  Binary Tree Longest Consecutive Sequence
# 2. Find Three Consecutive Integers That Sum to a Given Number
# 3. Maximum Consecutive Floors Without Special Floors
 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

def longest_consecutive(nums):  # T[n] : O(n)
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start checking for a sequence if the current number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Check for consecutive elements in increasing order
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

# Example usage:
nums = [100, 4, 200, 1, 3, 2]
result = longest_consecutive(nums)
print(result)  # Output: 4
