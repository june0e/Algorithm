def solution(progresses, speeds):
    answer = []
    count = 0
    
    while progresses: #작업물 있는동안 반복
        
        for x,y in enumerate(speeds): #진도 돌리기
            progress = int(progresses[x])
            speed = int(y)
            current_progress = progress + speed
            progresses[x] = current_progress
        while progresses and progresses[0] >= 100: #배포 가능한만큼 반복
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        if(count > 0):
            answer.append(count)
            count = 0  
    
    return answer