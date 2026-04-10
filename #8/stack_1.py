"""Problem Statement

Given an array arr of size n, for each element, find the next greater element to its right.
If no greater element exists, return -1 for that position.

📌 Example
Input:  [4, 5, 2, 10, 8]
Output: [5, 10, 10, -1, -1]"""

def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result

# Example
arr = [4, 5, 2, 10, 8]
print(next_greater_element(arr))