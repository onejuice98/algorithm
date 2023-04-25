import sys
from collections import deque
N = int(sys.stdin.readline())

ans = deque([])

for i in range(N, 0, -1):
    if not ans:
        ans.appendleft(i)
    else:
        ans.appendleft(i)
        for _ in range(i):
            ans.appendleft(ans.pop())

print(*ans)