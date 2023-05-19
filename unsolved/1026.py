import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = {}

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
        
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

for i in graph:
    graph[i] = sorted(graph[i])
    
""" dfs """
dfs_visited = []
def dfs(root):
    if len(dfs_visited) == N:
        return False
    if root not in dfs_visited and root in graph:
        dfs_visited.append(root)
        for i in graph[root]:
            dfs(i)

dfs(V)
print(*dfs_visited)

""" bfs """
bfs_visited = [V]

queue = deque([V])
while queue:
    next_cur = queue.popleft()
    if next_cur in graph:
        for i in graph[next_cur]:
            if i not in bfs_visited and i in graph:
                bfs_visited.append(i)
                queue.append(i)

print(*bfs_visited)