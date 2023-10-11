import sys

nums = [i for i in range(0, 10000)]

for i in range(1, 10000):
    if nums:
        total = i
        for char in str(i):
            total += int(char)
        if total < 10000:
            nums[total] = 0
        

for i in nums:
    if i:
        print(i)