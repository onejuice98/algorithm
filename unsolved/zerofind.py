def solution(s):
    answer = []
    
    next_s = s
    cnt_zero = 0
    temp = []
    while(len(next_s) != 1):
        for item in next_s:
            if item == "0":
                cnt_zero += 1
            else:
                temp.append("1")
        
        temp_length = len(temp)
    
        next_s = str(bin(temp_length)[2:])
        
        
    print(cnt_zero)
        
    return answer


solution("01110")