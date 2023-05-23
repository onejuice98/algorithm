import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

dfs_visited = [0] * (N+1)
""" dfs """
def dfs(root):
    dfs_visited[root] = 1
    print(root, end = " ")
    for i in range(1, N+1):
        if not dfs_visited[i] and graph[root][i]:
            dfs(i)



""" bfs """

def bfs(V):
    queue = [V]
    dfs_visited[V] = 0
    
    while queue:
        V = queue.pop(0)
        print(V, end = " ")
        for i in range(1, N+1):
            if dfs_visited[i] == 1 and graph[V][i] == 1:
                queue.append(i)
                dfs_visited[i] = 0


dfs(V)
print()
bfs(V)
