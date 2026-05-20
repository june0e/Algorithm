from functools import cmp_to_key
def compare(a,b):
    comp_a = str(a)+str(b)
    comp_b = str(b)+str(a)
    if int(comp_a) > int(comp_b):
        return -1
    elif int(comp_a) == int(comp_b):
        return 0
    else:
        return 1

def solution(numbers):
    answer = ''
    numbers.sort(key=cmp_to_key(compare))
    for i in numbers:
        answer += str(i)
    answer = int(answer)
    answer = str(answer)
    return answer

    