import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
nums = deque(list(map(int, sys.stdin.readline().split())))

queue = deque(range(1, N+1))
ans = 0

while nums:
    if nums[0] == queue[0]:
        nums.popleft()
        queue.popleft()
    else:
        if queue.index(nums[0]) > int(len(queue)/2):
            queue.appendleft(queue.pop())
            ans = ans + 1
        else:
            queue.append(queue.popleft())
            ans = ans + 1
        
print(ans)