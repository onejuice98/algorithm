import sys

N, M = map(int, sys.stdin.readline().split())

need_cash = []
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    if A < B:
        need_cash.append(B-N)

need_cash.sort()
need_cash.pop()
if need_cash:
    print(sum(need_cash))
else:
    print(0)