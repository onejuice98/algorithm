import sys
N = int(sys.stdin.readline())

ans = []
for i in range(N):
    temp = ""
    L = list(sys.stdin.readline().split())
    
    while len(L) != 0:
        temp += L.pop() + " "
        
    ans.append(f"Case #{i+1}: {temp}" )
    
    
for line in ans:
    print(line)