import sys
N = int(sys.stdin.readline())

heights = []
for i in range(N):
    height = int(sys.stdin.readline())
    
    while heights and heights[-1] <= height:
        heights.pop()
    heights.append(height)
    
print(len(heights))