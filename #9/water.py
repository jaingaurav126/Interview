arr=[1, 8, 6, 2, 5, 4, 8, 3, 7]
def maxArea(arr):
    n=len(arr)
    max_area=0
    left=0
    right=n-1
    while left<right:
        height=min(arr[left],arr[right])
        width=right-left
        area=height*width
        max_area=max(max_area,area)

        if arr[left]<arr[right]:    
            left+=1
        else:   
            right-=1        

    return max_area

print(maxArea(arr))