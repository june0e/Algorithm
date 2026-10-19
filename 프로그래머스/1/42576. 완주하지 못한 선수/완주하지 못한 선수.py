def solution(participant, completion):
    answer = ''
    counts = {}
    for name in participant:
        counts[name] = counts.get(name, 0) + 1
    for name in completion:
        counts[name]-=1
    
    for name,count in counts.items(): #꺼내기 
        if count == 1:
            answer = name
        
    return answer