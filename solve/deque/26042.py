import sys
from collections import deque;
N = int(sys.stdin.readline())

line = deque([]);
waiting = 0
student = 0
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))

    if a[0] == 1:
        line.append(a[1])
    elif a[0] == 2:
        line.popleft()
    
    if waiting < len(line):
        waiting = len(line)
        student = a[1]
    elif waiting == len(line) and student > a[1]:
        student = a[1]

print(waiting, student)
