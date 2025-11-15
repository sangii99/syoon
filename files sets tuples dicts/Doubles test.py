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

nums2 = [237, -263, -94, -173, 381, -257, -257, 6, -257, 6, -113, -145, 194, 6, -86, 244, -343, -287, -263, 244]
def double2(nums2):
    nums_count = {}
    for num in nums2:
        if num in nums_count:
            nums_count[num] += 1
        else:
            nums_count[num] = 1
    set1 = set()
    set2 = set()
    for num in nums_count:
        if nums_count[num] >= 2:
            set2.add(num)
        else:
            set1.add(num)
    return tuple((set1, set2))