import sys

N, M = map(int, (sys.stdin.readline().split()))

listen = {}
see_listen = []

for _ in range(N):
    name = str(sys.stdin.readline().rstrip())
    listen[name] = True

for _ in range(M):
    name = str(sys.stdin.readline().rstrip())
    if name in listen:
        see_listen.append(name)


print(len(see_listen))
see_listen.sort() 
for person in see_listen:
    print(person)
