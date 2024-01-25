# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9



def trap(height):
    if not height or len(height) < 3:
        return 0

    n = len(height)
    left, right = 0, n - 1
    left_max, right_max = height[left], height[right]
    trapped_water = 0

    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max < right_max:
            trapped_water += left_max - height[left]
            left += 1
        else:
            trapped_water += right_max - height[right]
            right -= 1

    return trapped_water

# Example usage:
elevation_map = [0,1,0,2,1,0,1,3,2,1,2,1]
result = trap(elevation_map)
print(result)
