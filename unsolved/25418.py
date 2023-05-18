# import sys

# A, K = map(int, sys.stdin.readline().split())
# ans = 0
# while True:
#     if A == K:
#         print(ans)
#         break
#     else:
#         if K // 2 >= A:
#             if K % 2 == 0:
#                 K = K // 2
#             else:
#                 K -= 1
#         elif K - 1 >= A:
#             K -= 1
#     ans += 1
