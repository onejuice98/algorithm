import sys

T = int(sys.stdin.readline())

def dfs(graph, cur_x, cur_y, M, N):
    if -1 < cur_y < M and -1 < cur_x < N and graph[cur_x][cur_y]:
        graph[cur_x][cur_y] = 0
        dfs(graph, cur_x-1, cur_y, M, N)
        dfs(graph, cur_x+1, cur_y, M, N)
        dfs(graph, cur_x, cur_y-1, M, N)
        dfs(graph, cur_x, cur_y+1, M, N)
        return True
    else:
        return False
    

for i in range(T):
    ans = 0
    N, M, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for _ in range(N)]
    
    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
        
    for a in range(N):
        for b in range(M):
            if graph[a][b] == 1:
                dfs(graph, a, b, M, N)
                ans += 1
    print(ans)