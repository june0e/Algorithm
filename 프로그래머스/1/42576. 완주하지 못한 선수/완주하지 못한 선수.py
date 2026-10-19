def solution(participant, completion):
    answer = ''
    counts = {}
    for i in participant:
        counts[i] = counts.get(i,0)+1
    for name in completion:
        counts[name] -= 1
    
    for name,count in counts.items():
        if count==1:
            answer = name
    return answer