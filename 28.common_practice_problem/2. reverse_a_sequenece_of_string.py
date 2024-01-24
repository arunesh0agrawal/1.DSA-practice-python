# Given a string, reverse that sequence

# Example 

# s = "my name is alex"
# output = "alex is name my"

# reversed(string) -> return a iteratot with reversed values, applicable on index(list or python)
original_string = "my name is alex"
reversed_string = " ".join(reversed(original_string.split()))
print(reversed_string)
