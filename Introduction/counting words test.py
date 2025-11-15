nums = [1, 2, 3, 4, 2]
num_count = {}
for num in nums:
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1

print(num_count)