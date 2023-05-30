import sys

P, K = map(int, sys.stdin.readline().split())

isBad = True
for i in range(2, K+12):
    if P % i == 0:
        print("BAD", i)
        isBad = False
        break

if isBad:
    print("GOOD")
    