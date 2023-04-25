import sys

N = int(sys.stdin.readline())

table = {}
is_bell = False
for _ in range(N):
    card, x = map(str, sys.stdin.readline().split())
    
    if card in table:
        table[card] += int(x)
    else:
        table[card] = int(x)

for card in table:
    if table[card] == 5:
        print("YES")
        is_bell = True
        break

if not is_bell:
    print("NO")
