import math 
def solution(arr):
    answer = 0
    # 배열 1번째와 2번째의 최소공배수 먼저 구하기
    answer = arr[0]*arr[1] // math.gcd(arr[0],arr[1])
    print(answer)
    for i in range(2,len(arr)):
        answer = answer * arr[i] // math.gcd(answer,arr[i])
    return answer