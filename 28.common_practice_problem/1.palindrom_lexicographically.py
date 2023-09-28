# problem statement :  given a string s,  using minimum no. of replacements modify the string s such that any permutation of string can be a palindrome. youhave to make replacements such that the resulting plaindrome is lexicographically the smallest.

# eg 1. aabbcc -> abccba
# eg2. ebbedda -> bdeaedb

def make_palindrome_lexicographically_smallest(s):
    # Create a frequency count of characters
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Initialize variables
    middle_char = ''
    left_half = ''
    right_half = ''

    # Iterate through characters and counts
    # T(n) : O(nlogn) [ Timsort by python]
    for char, count in sorted(char_count.items()):
        if count % 2 == 1:
            if middle_char:
                return "NO SOLUTION"  # Cannot form a palindrome
            middle_char = char
        left_half += char * (count // 2)
        right_half = char * (count // 2) + right_half

    # Construct the lexicographically smallest palindrome
    palindrome = left_half + middle_char + right_half

    return palindrome


# Example usage:
s = "ebcdecdab"
result = make_palindrome_lexicographically_smallest(s)
print(result)
