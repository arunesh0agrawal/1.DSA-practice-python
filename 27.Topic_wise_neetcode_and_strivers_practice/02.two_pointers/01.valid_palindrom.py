# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

def isPalindrome(s): # [ T(n): O(n), pythonic way is faster in terms of speed]
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())

    # Check if the cleaned string is a palindrome
    # Algorithmic way
    str_len = len(cleaned_s)
    for i in range(int(str_len/2)):
        if cleaned_s[i] != cleaned_s[str_len - 1 - i]:
            return False
    return True

    # pythonic way
    # return cleaned_s == cleaned_s[::-1]

# Example usage:
s = "A man, a plan, a canal: Panama"
result = isPalindrome(s)
print(result)  # Output: True
