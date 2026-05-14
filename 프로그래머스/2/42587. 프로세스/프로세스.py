from collections import deque

def solution(priorities, location):
    q_priorities = deque()
    for idx, priority in enumerate(priorities):
        q_priorities.append((idx,priority))
    target_idx, target_priority = q_priorities[location]
    answer = 0
    
    while q_priorities:
        cur_idx,cur_priority = q_priorities.popleft()
        if any(priority > cur_priority for idx, priority in q_priorities):
            q_priorities.append((cur_idx,cur_priority))
        else:
            answer+=1
            if(target_idx == cur_idx):
                break
            
    print(answer)
    return answer