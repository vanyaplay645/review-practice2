def even(nums):
    res = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            res.append(nums[i])
    return res