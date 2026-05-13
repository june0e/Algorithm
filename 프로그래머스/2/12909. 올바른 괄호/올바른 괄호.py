def solution(s):
    answer = True
    count_left = 0
    count_right = 0
    
    for i,char_s in enumerate(s):
        if(i == 0):
            if( char_s != "("):
                return False 
            
        if char_s == "(":
             count_left += 1
        if char_s == ")":
                count_right += 1
        if count_left < count_right:
            return False 
    if(count_left != count_right):
        return False
    return answer
        

    