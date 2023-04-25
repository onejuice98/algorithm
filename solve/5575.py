cnt = 0
answer = []
while cnt < 3:
    A = list(map(int, input().split()))

    result = [0, 0, 0]

    for i in range(2, -1, -1):
        result[i] += A[3 + i] - A[i]

        if result[i] < 0:
            result[i - 1] -= 1
            result[i] += 60
            
        
    answer.append(result)
    cnt += 1
    
for i in answer:
    print(*i)