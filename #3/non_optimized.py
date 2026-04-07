"""🧩 Problem: Two Sum

Given:

An array of integers nums
A target integer target

Task:
Return the indices of the two numbers such that they add up to target.

👉 You cannot use the same element twice
👉 Exactly one solution exists"""

#Step 1: Brute Force Approach (What NOT to stop at)
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 7, 11, 15]
target = 26
print(twoSum(nums, target))


"""⏱ Time Complexity: O(n²)
❌ Too slow for interviews"""