import sys

len_stores = int(sys.stdin.readline())

stores = list(map(int, sys.stdin.readline().split()))

how_many_milk_drink = 0
for store in stores:
    if how_many_milk_drink % 3 == store:
        how_many_milk_drink += 1 
    
print(how_many_milk_drink)