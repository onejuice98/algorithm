import sys

T = int(sys.stdin.readline())

answers = []

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(int(factorial(M) / ((factorial(M-N)) * factorial(N))))
    