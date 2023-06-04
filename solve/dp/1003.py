import sys

T = int(sys.stdin.readline())

fibo_dict = {
    0 : [1, 0],
    1 : [0, 1]
}
def fibo(num):
    if num < 2:
        return fibo_dict[num]
    else:
        for i in range(2, num+1):
            fibo_dict[i] = [0, 0]
            fibo_dict[i][0] = fibo_dict[i-2][0] + fibo_dict[i-1][0]
            fibo_dict[i][1] = fibo_dict[i-2][1] + fibo_dict[i-1][1]


fibo(40)
for _ in range(T):
    N = int(sys.stdin.readline())
    print(*fibo_dict[N])
    