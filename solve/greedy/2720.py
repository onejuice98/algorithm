import sys

T = int(sys.stdin.readline())

ans = []
def calc_remain(money):
    if money < 5:
        cents[3] += money
        return None;
    if money >= 25:
        cents[0] += 1
        return calc_remain(money-25)
    elif money >= 10:
        cents[1] += 1
        return calc_remain(money-10)
    elif money >= 5:
        cents[2] += 1
        return calc_remain(money-5)

for _ in range(T):
    cents = [0, 0, 0, 0]
    cent = int(sys.stdin.readline())
    calc_remain(cent)
    print(*cents)