"""Problem: Maximum Sum Subarray of Size K
Given:
An array
A number K

Example:

arr = [2, 1, 5, 1, 3, 2]

K = 3

🎯 Goal

👉 Find the maximum sum of any subarray of size K"""      

def max_sum_subarray(arr, k):    
    max_sum=0
    window_sum=0
    window_start=0
    n=len(arr)
    for i in range(n):
        window_sum=window_sum+arr[i]
        if i>=k-1:
            max_sum=max(max_sum,window_sum)
            window_sum=window_sum-arr[window_start]
            window_start=window_start+1
        

    return max_sum

            
            



arr = [2, 1, 5, 1, 3, 10]
k = 3
print(max_sum_subarray(arr, k))  # Output: 9