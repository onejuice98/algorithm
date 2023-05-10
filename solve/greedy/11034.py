import sys

while True:
    try:
        kangs = sys.stdin.readline()
        A, B, C = map(int, kangs.split())
        print(max(B-A, C-B)-1)
    except:
        break
    
    
