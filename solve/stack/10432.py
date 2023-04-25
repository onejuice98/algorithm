import sys

P = int(sys.stdin.readline())


answer = []
for _ in range(P):
    T = list(map(int, sys.stdin.readline().split()))
    island = []
    stack = []
    
    for i in range(2, 13):
        
        while stack and stack[-1] > T[i]:
            island.append(stack.pop())
        
        if not stack or stack[-1] != T[i]:
            stack.append(T[i])
    answer.append((T[0], len(island)))
    
for i in answer:
    print(*i)
