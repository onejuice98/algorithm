
N = int(input())
list = list(map(int, input().split()))

result = []
for i in range(len(list)):
    if (i == 0):
        result.append(i + 1)
    else:
        result.insert(list[i], i + 1)

result.reverse()
    
print(*result)