def solution(s):
    answer = ''
    answer_arr = sorted(s,reverse=True)

    return answer.join(answer_arr)