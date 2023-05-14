import sys

N, M = map(int, sys.stdin.readline().split())

boxs = {}
for i in range(N):
    boxs[i+1] = 0
    
for cur in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for cnt in range(i, j+1):
        boxs[cnt] = k

print(*boxs.values())