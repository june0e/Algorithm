def solution(number, k):
    answer = ''
    num = k
    answer_list = []
    for cnt,i in enumerate(number):
        i = int(i)
        if cnt == 0 : 
            answer_list.append(i)
        else:
            if answer_list[-1] < i:
                while answer_list and answer_list[-1] < i  and k > 0:
                    answer_list.pop()
                    k-=1
                answer_list.append(i)
            else:
                answer_list.append(i)
                
    if k > 0:
        answer_list = answer_list[:-k]
    answer = ''.join(map(str,answer_list))

    return answer