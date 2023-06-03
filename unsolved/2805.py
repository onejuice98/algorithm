import sys

N, M = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

sp, rp = 1, max(trees)   

while sp <= rp:
    mp = (sp + rp) // 2
    
    tree_sum = 0
    for tree in trees:
        if tree >= mp:
            tree_sum += tree - mp
    if tree_sum >= M:
        sp = mp + 1
    else:
        rp = mp - 1
print(rp)