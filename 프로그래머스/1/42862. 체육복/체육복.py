def solution(n, lost, reserve):
    #전체학생수 n
    # 도난당한 학생들의 번호 배열 lost
    # 여벌의 체육복을 가져온 학생들의 번호 reserve 
    # 여벌의 체육복은 앞뒤사람한테만 빌려줄 수 있고 
    # 체육 수업을 들을 수 있는 학생의 수 구하기
    
    answer = n - len(lost) # 1.잃어버린 학생을 제외한 학생들
    
    lost.sort()
    reserve.sort()
    
    #2. 여벌 체육복 가져온 학생이 체육복을 도난 당한사람 제거
    for i in lost[:]:
        if i in reserve:
                answer+=1 
                reserve.remove(i)
                lost.remove(i)
    
    for i in lost:
        if i-1 in reserve: # 3.잃어버린 학생 앞번호 친구가 여분의 체육복이 있는지 확인
            answer += 1
            reserve.remove(i-1)
        elif i+1 in reserve: # 4.잃어버린 학생 뒷번호 친구가 여분의 체육복이 있는지 확인
            answer += 1 
            reserve.remove(i+1)

    return answer