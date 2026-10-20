def solution(s):
    answer = True
    status = 0
    for i,j in enumerate(s):

        if i == 0:
            if j != '(':
                return False
            else:
                status += 1
                continue
        if j == '(':
            status += 1
        else:
            status -= 1
            
        if status < 0 :
            return False
    if status > 0:
        return False

    return True