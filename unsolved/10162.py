# import sys

# T = int(sys.stdin.readline())

# A = 300
# B = 60
# C = 10

# answer = [0, 0, 0]
# while T >= 10:
#     if T > A:
#         answer[0] += 1
#         T -= A
#     else:
#         if T > B:
#             answer[1] += 1
#             T -= B
#         else:
#             answer[2] += 1
#             T -= C
            
# if T != 0:
#     print(-1)
# else:
#     print(*answer)