
"""🔥 Problem: Largest Rectangle in Histogram
🧩 Problem Statement

You are given an array where each element represents the height of bars in a histogram.

👉 Find the largest rectangular area possible."""

def largestRectangleArea(heights):
    n=len(heights)
    max_area=0
    stack=[]
    for i in range(n):
        while stack and heights[stack[-1]]>heights[i]:
            h=heights[stack.pop()] 
            if stack:
                width=i-stack[-1]-1 

            else:
                width=i
            
            max_area=max(max_area,h*width)

        stack.append(i)

    while stack:
        h=heights[stack.pop()]   
        if stack:
            width=n-stack[-1]-1  

        else:
            width=n
            
        max_area=max(max_area,h*width)





    return max_area








arr=[2, 1, 5, 6, 2, 3]
print(largestRectangleArea(arr))


