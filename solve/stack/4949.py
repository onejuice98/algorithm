import sys

while True:
    line = sys.stdin.readline()
    stack = []
    if line[0] == ".":
        break   
    
    for i in line:
        if i == "(":
            stack.append(")")
        elif i == "[":
            stack.append("]")
        elif i == ")":
            if not stack or stack.pop() != i:
                print("no")
                break
        elif i == "]":
            if not stack or stack.pop() != i:
                print("no")
                break
        if not stack and i == '.':
            print("yes")
        if stack and i == '.':
            print("no")
    
 