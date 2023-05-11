import sys

N = int(sys.stdin.readline())

place_costs = list(map(int, sys.stdin.readline().split()))

print(sum(place_costs)-max(place_costs))