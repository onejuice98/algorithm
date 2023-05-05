import sys

N = int(sys.stdin.readline())

nums = []
num_count = {}

for i in range(N):
    num = sys.stdin.readline().rstrip()
    for char in num:
        if char not in num_count:
            num_count[char] = 1
        else:
            num_count[char] += 1
    nums.append(num)

K = int(sys.stdin.readline())

sorted_num_count = sorted(num_count.items(), key = lambda item : item[1])
change_char = {}

for idx, val in enumerate(sorted_num_count):
    if idx == K:
        break
    change_char[val[0]] = True

for i in range(N):
    for char in nums[i]:
        if char in change_char:
            nums[i] = nums[i].replace(char, 'Z')

nums_to_int = []
for i in range(N):
    adder = 0
    for idx, char in enumerate(nums[i]):
        if ord(char) < 55:
            adder += int(char) *36 ** (len(nums[i]) - idx - 1)
        else:
            adder += (ord(char)-55) *36 ** (len(nums[i]) - idx - 1)
    nums_to_int.append(adder)

temp = sum(nums_to_int)
answer = ''
while temp > 36:
    if temp%36 > 10:
        answer += chr(temp%36 + 55)
    else:
        answer += str(temp%36)
    temp = int(temp/36)
if temp != 0:
    if temp%36 > 10:
        answer += chr(temp%36 + 55)
    else:
        answer += str(temp%36)
    # if temp / 36 > 10:
    #     answer += chr(int(temp/36) + 55)
    # else:   
    #     answer += str(int(temp/36))
print(answer[::-1])
# print(sorted_num_count)
# print(change_char)