'''Given a string, find the longest substring without repeating characters.'''

def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    start_index = 0   # to track start of best substring

    for right in range(len(s)):
        # Shrink window if duplicate found
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            print("value of left:", left)

        # Add current character
        char_set.add(s[right])

        # Update max substring info
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start_index = left

    # Return substring
    return s[start_index:start_index + max_length]


# Driver code
s = "abcdccbescfwewr"
print("Longest substring:", longest_unique_substring(s))