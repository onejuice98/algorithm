import sys


while True:
    
    test_case = sys.stdin.readline()
    if not test_case:
        break
    s, t = test_case.split()
    cnt = 0
    match_point = 0
    
    for char in s:
        while cnt < len(t):
            if t[cnt] == char:
                match_point += 1
                cnt += 1
                break
            else:
                cnt += 1        
                
    if match_point == len(s):
        print("Yes")
    else:
        print("No")
