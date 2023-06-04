import sys

N = int(sys.stdin.readline())

def facto(num):
    if num == 0:
        return 1
    return num * facto(num-1)

count_N = str(facto(N))

ans = 0
for i in count_N[::-1]:
    if i == '0':
        ans += 1
    else:
        break

print(ans)
