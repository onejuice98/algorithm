import sys

words = list(sys.stdin.readline())
words.pop()

M = int(sys.stdin.readline())

storage = []
for _ in range(M):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == "L" and words:
        storage.append(words.pop())
    elif cmd[0] == "D" and storage:
        words.append(storage.pop())
    elif cmd[0] == "B" and words:
        words.pop()
    elif cmd[0] == "P":
        words.append(cmd[1])
        

answer = ""
for i in words:
    answer += i
while storage:
    answer += storage.pop()
    
print(answer)
