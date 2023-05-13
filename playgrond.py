def solution(ages):
    age=''
    candle=[0,0,0,0,0,0,0,0,0,0]
    for i in range(len(ages)):
        age+=str(ages[i])
    age=list(age)
    for i in range(len(age)):
        if age[i]=='6':
            age[i]='9'
    for i in age:
        candle[int(i)]+=1
        if candle[9]%2==0:
            candle[9]=candle[9]//2
        else:
            candle[9]=candle[9]//2+1       
    return max(candle)

ages = [6, 9, 6]

needed = {}
for age in ages:
    for char in str(age):
        if char not in needed:
            if char == "6" or char == "9":
                needed[char] = 0
            else:
                needed[char] = 1
        else:
            needed[char] += 1

if max(needed.values()) == 0:
    print(1)
else: 
    print(max(needed.values()))