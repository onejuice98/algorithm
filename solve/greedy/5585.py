import sys

money = 1000-int(sys.stdin.readline())

cents_cnt = [0, 0, 0, 0, 0, 0]

def calc_cents_cnt(remainer):
    if remainer < 5:
        cents_cnt[0] += remainer
        return sum(cents_cnt)
    if remainer >= 500:
        cents_cnt[0] += 1
        return calc_cents_cnt(remainer-500)
    if remainer >= 100:
        cents_cnt[0] += 1
        return calc_cents_cnt(remainer-100)
    if remainer >= 50:
        cents_cnt[0] += 1
        return calc_cents_cnt(remainer-50)
    if remainer >= 10:
        cents_cnt[0] += 1
        return calc_cents_cnt(remainer-10)
    if remainer >= 5:
        cents_cnt[0] += 1
        return calc_cents_cnt(remainer-5)

print(calc_cents_cnt(money))