# import sys

# T = int(sys.stdin.readline())

# for _ in range(T):
#     a, b = map(int, (sys.stdin.readline()).split())
#     temp = a % 10
    
#     if temp == 0:
#         print(10)
#     elif temp in [1, 5, 6]:
#         print(temp)
#     elif temp in [4, 9]:
#         temp_b = b % 2
#         if temp_b == 0:
#             print(temp * temp % 10)
#         else:
#             print(temp)
#     else:
#         temp_b = b % 4
#         if temp_b == 0:
#             print(temp ** 4 % 10)
#         else:
#             print(temp ** temp_b % 10)
    

list3 = [1, 2, 3]
list3.reverse()
print(list3)