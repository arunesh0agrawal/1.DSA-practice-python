# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 # Releated Pronlems : 
# 1) 3sum
# 2) 4sum
# 3) two sum ( input array is sorted)

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


def two_sum(nums, target): # [ T(n): O(n)]
    # Dictionary to store the indices of elements
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num

        # Check if complement is already in the dictionary
        if complement in num_indices:
            # Return the indices of the two numbers
            return [num_indices[complement], i]

        # If complement is not found, store the current index
        num_indices[num] = i

    # If no solution is found, return an empty list or handle it as needed
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]
