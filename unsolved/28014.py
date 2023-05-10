import sys

N = int(sys.stdin.readline())

heights = list(map(int, sys.stdin.readline().split()))

cnt = 0
for idx, height in enumerate(heights):
    if idx == 0:
        cnt += 1
    else:
        if heights[idx-1] > height:
            pass
        else:
            cnt += 1
print(cnt)