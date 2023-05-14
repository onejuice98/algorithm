import sys
from collections import deque
N = int(sys.stdin.readline())

pairs = int(sys.stdin.readline())

graph = {}
for _ in range(pairs):
    a, b = map(int, sys.stdin.readline().split())
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

queue = deque([1])
visited = []


while queue:
    temp = queue.popleft()
    for i in graph[temp]:
        if i not in visited:
            visited.append(i)
            queue.append(i)
            
print(len(visited)-1)