import sys

N, M = map(int, sys.stdin.readline().split())

leaf = 0
if M == 2:
    leaf = 1

last_leaf = 0
for i in range(1, N):
    if M > leaf:
        print(0, i)
        leaf += 1
    else:
        print(last_leaf, i)
    last_leaf = i