import sys

N = int(sys.stdin.readline())
times = [4, 6, 4, 10]
table = {}
for _ in range(N):
    for time in times:
        workers = list(map(str, sys.stdin.readline().split()))
        
        for worker in workers:
            if worker != '-':
                if worker in table:
                    table[worker] += time
                else:
                    table[worker] = time

max_time = 0
min_time = 9999999
for worker in table:
    if table[worker] > max_time:
        max_time = table[worker]
    if table[worker] < min_time:
        min_time = table[worker]

if max_time - min_time <= 12:
    print("Yes")
else:
    print("No")
    
    