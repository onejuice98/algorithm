def solution(n, m, section):
    floor = [True] * n
    for i in section:
        floor[i-1] = False
    
    cnt = 0
    cur = 0
    while not all(floor) and cur < len(section):
        cursor = section[cur] -1
        if not floor[cursor]:
            for i in range(cursor, cursor+m):
                floor[i] = True
            cnt += 1
        cur += 1
        
        
    return cnt

print(solution(8,4,[2, 3, 6]))