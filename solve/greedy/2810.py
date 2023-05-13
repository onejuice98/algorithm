import sys

N = int(sys.stdin.readline())

seats = str(sys.stdin.readline()).rstrip()

seats_type_count = {"S" : 0, "L" : 0}

for seat in seats:
    seats_type_count[seat] += 1

can_use_holder = N+1 - int(seats_type_count["L"]/2)
if can_use_holder >= N:
    print(N)
else:
    print(can_use_holder)