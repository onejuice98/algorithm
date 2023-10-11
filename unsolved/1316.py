import sys

n = int(sys.stdin.readline())
ans = n
for _ in range(n):
    word = str(sys.stdin.readline().rstrip())
    stack = []
    group = {}
    for char in word:
        if char not in group:
            group[char] = True
        else:
            if stack[-1] == char:
                continue
            ans -= 1
            break
        stack.append(char)
            
        
print(ans)