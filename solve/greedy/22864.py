import sys

A, B, C, M = map(int, sys.stdin.readline().split())

def calc_can_work(tired, work, rest):
    if work+rest == 24:
        return work, rest
    
    if tired + A <= M:
        return calc_can_work(tired + A, work + 1, rest)
    
    else:
        tired -= C
        if tired < 0:
            tired = 0
        return calc_can_work(tired, work, rest+1)
    
work, rest = calc_can_work(0, 0, 0)
print(work * B)