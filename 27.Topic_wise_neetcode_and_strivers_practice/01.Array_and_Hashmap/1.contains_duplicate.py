# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Releated Pronlems : 
# 1) contains duplicate II
# 2) contains dupliacte iii
# 3) make array zero by subtracting equal zero

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

# Example usage:
nums1 = [1, 2, 3, 1]
print(containsDuplicate(nums1))  # Output: True

nums2 = [1, 2, 3, 4]
print(containsDuplicate(nums2))  # Output: False

nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(nums3))  # Output: True


# The time complexity of this solution is O(n), where n is the length of the input array nums