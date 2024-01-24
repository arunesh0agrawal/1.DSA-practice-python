# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 # Releated Pronlems : 
# 1) group shigted strings
# 2) find resultant array after removing anagrams
# 3) Count anagrams

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

def group_anagrams(strs): # [ T(n) : O(n * m * log(m))]
    anagram_groups = {}

    for word in strs:
        # Use a sorted tuple of characters as the key
        key = tuple(sorted(word))
        print(key)

        # Add the word to the corresponding group
        anagram_groups.setdefault(key, []).append(word)

    # Return the values of the dictionary as the result
    return list(anagram_groups.values())

# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)
