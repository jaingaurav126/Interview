"""🧩 Problem: Longest Consecutive Sequence

🧪 Example
[100, 4, 200, 1, 3, 2]

Consecutive sequences:

[1,2,3,4] → length = 4 ✅
[100] → 1
[200] → 1

👉 Answer = 4"""

def longest_consecutive_sequence(ar):
    max_length=0
    length=1
    for num in ar:
        while num+1 in d:
            length+=1
            num+=1

        max_length=max(length, max_length)
        length=1
    return max_length




ar=[98,99,100,101,102,103, 4, 200, 1, 3, 2]
d=set(ar)
print(longest_consecutive_sequence(ar))




    
