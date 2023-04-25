import sys

N = int(sys.stdin.readline())
ans = 0
for i in range(N):
    stack = []
    words = sys.stdin.readline()
    for word in words:
        if stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)
    
    if len(stack) == 1:
        ans = ans + 1
        
print(ans)