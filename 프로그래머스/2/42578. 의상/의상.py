def solution(clothes):
    dic = {}

    for name, kind in clothes:
        dic[kind] = dic.get(kind, 0) + 1

    answer = 1

    for count in dic.values():
        answer *= count + 1

    return answer - 1