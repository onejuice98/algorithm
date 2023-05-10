import sys

time = int(sys.stdin.readline())

btn = [0, 0, 0]
def calc_btn(remain_time):
    if remain_time < 10:
        if remain_time == 0:
            print(*btn)
        else:
            print(-1)
        return None
    if remain_time >= 300:
        btn[0] += 1
        return calc_btn(remain_time-300)
    if remain_time >= 60:
        btn[1] += 1
        return calc_btn(remain_time-60)
    if remain_time >= 10:
        btn[2] += 1
        return calc_btn(remain_time-10)

calc_btn(time)
