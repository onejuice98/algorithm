import sys

N = int(sys.stdin.readline())

coordinates = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinates.append((x, y))
    
coordinates.sort(key= lambda x : (x[1], x[0]))

for coord in coordinates:
    print(*coord)