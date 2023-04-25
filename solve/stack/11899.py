import sys
S = list(sys.stdin.readline())
S.pop()

stack = []

for i in S:
    if i == "(":
        stack.append(")")
    else:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append("(")

print(len(stack))