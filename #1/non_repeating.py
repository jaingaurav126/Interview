"""Question: First Non-Repeating Character

Problem:
Given a string, return the first non-repeating character.
If none exists, return -1."""

def first_non_repeating(s):
    # Step 1: Create dictionary to store frequency
    freq = {}

    # Step 2: Count frequency of each character
    for ch in s:
        if ch in freq:
            freq[ch] += 1   # increment count
        else:
            freq[ch] = 1    # first occurrence

    # Step 3: Find first character with frequency 1
    for ch in s:
        if freq[ch] == 1:
            return ch

    # Step 4: If no non-repeating character
    return -1


# Driver code
s = "aabbcdeff"
result = first_non_repeating(s)

if result == -1:
    print("No non-repeating character found")
else:
    print("First non-repeating character:", result)