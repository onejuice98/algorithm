import sys

A, B = map(str, sys.stdin.readline().split())

min_A = int(A.replace("6", "5"))
min_B = int(B.replace("6", "5"))

max_A = int(A.replace("5", "6"))
max_B = int(B.replace("5", "6"))

print(min_A + min_B, max_A + max_B)