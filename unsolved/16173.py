import sys

N = int(sys.stdin.readline())

graph = []
for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    graph.append(line)

visited = [[0] * N for _ in range(N)]

def dfs(i, j):
    if i < 0 or i > N-1 or j < 0 or j > N-1 or visited[i][j]:
        return False
    visited[i][j] = 1
    if graph[i][j] == -1:
        visited[i][j] = 1
        return True
    
    dfs(i, j + graph[i][j])
    dfs(i + graph[i][j], j)

    
dfs(0,0)
if visited[-1][-1]:
    print("HaruHaru")
else:
    print("Hing")