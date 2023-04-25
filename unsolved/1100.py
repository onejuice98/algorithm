import sys

answer =0
rlwns = 0
for line_num in range(8):
    line = sys.stdin.readline()
    if line_num % 2 == 0:
        rlwns = 0
    else:
        rlwns = 1
    for idx, elem in enumerate(line):
        if idx % 2 == rlwns and elem == 'F':
            answer += 1
print(answer)
