def all_non_repeating(s):
    # Step 1: Count frequency
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Step 2: Collect all non-repeating characters
    result = []

    for ch in s:
        if freq[ch] == 1:
            result.append(ch)

    return result


# Driver code
s = "aabbcdeff"
print("Non-repeating characters:", all_non_repeating(s))