#각 큐의 원소 합을 같게 만들기 위해 
from collections import deque 
def solution(queue1, queue2):
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    limit = 3*len(queue1)
    
    while answer < limit :
        
        if sum1 == sum2:
            return answer
        
        if sum1 > sum2:
            x = queue1.popleft()
            queue2.append(x)
            sum1 -= x
            sum2 += x
            
        else :
            x = queue2.popleft()
            queue1.append(x)
            sum2 -= x
            sum1 += x
        answer+=1
    return answer if sum1 == sum2 else -1