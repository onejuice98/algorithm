import sys

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)
    
nums.sort()
for num in nums:
    print(num)