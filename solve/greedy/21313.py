import sys

N = int(sys.stdin.readline())

octopus = []

for i in range(N):
    legs = {}
    for j in range(8):
        legs[j+1] = True
    octopus.append(legs)
    
cur = 0
ans = []

while cur < N:
    for num in range(1, 9):
        if cur + 1 < N:
            if octopus[cur][num] and octopus[cur+1][num]:
                octopus[cur][num] = False
                octopus[cur+1][num] = False
                ans.append(num)
                break
        else:
            if octopus[cur][num] and octopus[0][num]:
                octopus[cur][num] = False
                octopus[0][num] = False
                ans.append(num)
                break
    cur += 1
    
print(*ans)