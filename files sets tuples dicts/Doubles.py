def double(nums):
    nums_count = {}
    for num in nums:
        if num in nums_count:
            nums_count[num] += 1
        else:
            nums_count[num] = 1
    ans = None
    for num in nums_count:
        if nums_count[num] >= 2:
            ans = num
    return ans

def doubles(nums2):
    nums_count = {}
    double(nums2)
