import sys

N = int(sys.stdin.readline())


ans = [0, 0]
def sweet_box(amount):
    if amount == 0:
        return 0
    if amount < 3:
        return -1
    elif amount % 5 == 0:
        ans[1] += int(amount/5)
        return sweet_box(amount-5 * int(amount / 5))
    elif amount % 3 == 0:
        ans[0] += int(amount/3)
        return sweet_box(amount-3 * int(amount / 5))
    elif amount > 5:
        ans[1] += 1
        return sweet_box(amount-5)
    elif amount > 3:
        ans[0] += 1
        return sweet_box(amount-3)

if N % 5 > 3:
    print(-1)
else:
    sweet_box(N)
    print(sum(ans))