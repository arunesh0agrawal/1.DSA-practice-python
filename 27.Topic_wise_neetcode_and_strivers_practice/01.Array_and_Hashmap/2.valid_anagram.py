# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# pythonic way( not a good way)

# def isAnagram(s: str, t: str) -> bool: # [ T(o) = O(nlog(n))] 
#     return sorted(s) == sorted(t)

# print(isAnagram("anagram", "nagaram"))

# Algorithmic way [ optimized way]
def isAnagram(s: str, t: str) -> bool: # [ T(O) : O(n)]
    if len(s)!=len(t):
        return False
    
    freq_counter = {}
    
    # count freqency and store in dict, use get to access
    for alp in s:
        freq_counter[alp] = freq_counter.get(alp, 0) + 1

    # decrease counter in another string to find the anagram
    for char in t:
        if char not in freq_counter or freq_counter[char] == 0:
            return False
        freq_counter[char] -= 1
    
    # # Check if all frequencies are zero
    # return all(count == 0 for count in char_count.values()) # use of all ( to count all values all true)
        
    return True
print(isAnagram("anagram", "nmgraaa"))


    
