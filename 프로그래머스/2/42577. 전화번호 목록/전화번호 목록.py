def solution(phone_book):
    answer = True
    phone_num = set(phone_book)
    for num in phone_num:
        for i in range(1,len(num)):
            prefix = num[:i]
            if prefix in phone_num:
                return False
    
    return answer