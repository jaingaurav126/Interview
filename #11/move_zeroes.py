def move_zeroes(nums):
    j = 0  # position for next non-zero

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums
arr=[0,1,0,3,12]
print(move_zeroes(arr))

