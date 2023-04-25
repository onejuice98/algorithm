import sys
N = int(sys.stdin.readline())

skills = list(sys.stdin.readline())
skills.pop()

Rstack =[]
Kstack = []
ans = []

for s in skills:
    if s == "L":
        Rstack.append("R")
    elif s == "S":
        Kstack.append("K")
    
    elif s == "R":
        if Rstack and Rstack[-1] == s:
            ans.append(Rstack.pop())
        else:
            break
    elif s == "K":
        if Kstack and Kstack[-1] == s:
            ans.append(Kstack.pop())
        else:
            break
    else:
        ans.append(s)
            
print(len(ans))
        