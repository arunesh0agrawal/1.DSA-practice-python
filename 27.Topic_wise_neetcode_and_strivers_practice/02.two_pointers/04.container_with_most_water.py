# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 


def max_area(height):
    max_water = 0
    left, right = 0, len(height) - 1

    while left < right:
        # Calculate the area between the two pointers
        h = min(height[left], height[right])
        w = right - left
        current_water = h * w

        # Update the maximum water if the current area is greater
        max_water = max(max_water, current_water)

        # Move the pointers based on the shorter height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Example usage:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = max_area(height)
print(result)
