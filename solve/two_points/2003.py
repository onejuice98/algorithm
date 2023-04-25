
# 다시 푸셈
N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
answer = 0
while right <= N and left <= right:
    
    sum_list = nums[left:right]
    temp = sum(sum_list)
    
    if temp == M:
        answer += 1
        
        right += 1
        
    elif temp < M:
        right += 1
    else:
        left += 1

print(answer)