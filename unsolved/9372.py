import sys

T = int(sys.stdin.readline())
ans = []
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    
    table = {}
    cnt = 0
    do_nothing = False
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        
        if not do_nothing:
            if a not in table:
                table[a] = 1
                cnt += 1
            if b not in table:
                table[b] = 1
                cnt += 1 
        if len(table) == N:
            do_nothing = True
            
    ans.append(cnt-1)
    
    
for i in ans:
    print(i)
        