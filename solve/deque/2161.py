from collections import deque;
N = int(input())

cards = deque(range(1, N+1))
ans = []
cnt = 0
while len(cards) != 1:
    if cnt % 2 == 0:
        ans.append(cards.popleft())
    else:
        cards.append(cards.popleft())
    cnt = cnt + 1
    
ans.append(cards.popleft())

print(*ans)