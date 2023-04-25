import sys

N = int(sys.stdin.readline())

table = {}

for i in range(N):
    pwd = sys.stdin.readline().rstrip()

    table[pwd] = True
    
    if pwd[::-1] in table:
        print(len(pwd), pwd[int(len(pwd)/2)])
    
    
    