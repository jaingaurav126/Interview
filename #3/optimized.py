"""🧩 Problem: Two Sum

Given:

An array of integers nums
A target integer target

Task:
Return the indices of the two numbers such that they add up to target.

👉 You cannot use the same element twice
👉 Exactly one solution exists"""

"""💡 Key Idea:

Instead of checking every pair, store numbers in a dictionary as you go.

At each step:

Compute: complement = target - current number
Check if complement already exists"""


def twoSum(nums, target):
    hashmap = {}  # value -> index

    for i, num in enumerate(nums):
        print("value of i:", i, "value of num:", num)
        complement = target - num 

        if complement in hashmap:
            print("value of complement:", complement, "found at index:", hashmap[complement])
            return [hashmap[complement], i]

        hashmap[num] = i
        

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))


"""⏱ Time Complexity: O(n)          """
