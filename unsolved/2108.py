import sys
import math
N = int(sys.stdin.readline())

nums = []
how_many_nums = {}
most_values = []
most_times = 0
for _ in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)
    if num not in how_many_nums:
        how_many_nums[num] = 1
    else:
        how_many_nums[num] += 1

for value in how_many_nums:
    if most_times < how_many_nums[value]:
        most_times = how_many_nums[value]
        most_values = [value]
    elif most_times == how_many_nums[value]:
        most_values.append(value)

nums.sort()
most_values.sort(reverse=True)

print(math.floor(sum(nums)/N + 0.5))
print(nums[int((N-1)/2)])
if len(most_values) == 1:
    print(most_values[0])
else:
    print(most_values[-2])
print(nums[-1] - nums[0])
