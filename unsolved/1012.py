import sys
from collections import deque

T = int(sys.stdin.readline())

delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for _ in range(N)] 
    
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    
    queue = deque()
    ans = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i, j))
                ans += 1

                while queue:
                    cur_y, cur_x = queue.popleft()
                    graph[cur_y][cur_x] = -1
                    for k in range(4):
                        dy = cur_y + delta[k][0]
                        dx = cur_x + delta[k][1]
                        if 0 <= dy < N and 0 <= dx < M:
                            if graph[dy][dx] == 1:
                                graph[dy][dx] = -1
                                queue.append((dy, dx))
                
    print(ans)