import sys

N = int(sys.stdin.readline())

mins_array = list(map(int,sys.stdin.readline().split()))


min_num = mins_array[0]
ans = [0 for i in range(N)]

for i in range(1, N):
    ans[i] = max(ans[i-1], mins_array[i] - min_num)
    min_num = min(min_num, mins_array[i])
    
print(*ans)