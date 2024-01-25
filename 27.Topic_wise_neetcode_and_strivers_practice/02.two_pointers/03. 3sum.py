# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.



def threeSum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                right -= 1

            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
print(result)



# # my solution( not passsing complete cases)
# def threeSum(nums):
#     results = []
#     left, right = 0, len(nums) - 1

#     nums.sort()
#     print(nums)

#     while left < right and (left + 1 != right) and (right - 1 != left) :

#         current_sum = nums[left] + nums[right]

#         if current_sum < 0:
#             third_val = nums[right - 1]
#             new_sum = current_sum + third_val
#             if new_sum == 0:
#                 results.append([left, right - 1, right])
#             elif new_sum < 0:
#                 left += 1
#             else:
#                 right -= 1
#         elif current_sum >= 0:
#             third_val = nums[left + 1]
#             new_sum = current_sum + third_val
#             if new_sum == 0:
#                 results.append([nums[left], nums[left + 1], nums[right]])
#                 left += 1
#             elif new_sum < 0:
#                 left += 1
#             else:
#                 right -= 1

#     return results


# # Example usage:
# nums = [-4, -1, -1, 0, 1, 2]
# nums1 = [0,0,0]
# nums2  =[0,1,1]
# result = threeSum(nums2)
# print(result)
