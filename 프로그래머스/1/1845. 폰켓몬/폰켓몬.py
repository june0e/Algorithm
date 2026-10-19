def solution(nums):
    answer = 0
    counts ={}
    value = []
    for phoneketmon in nums:
        counts[phoneketmon] = counts.get(phoneketmon,0)+1
    
    for phoneketmon,count in counts.items():
        value.append(phoneketmon)
    if len(value) >= len(nums)//2:
        answer = len(nums)//2
    else:
        answer =len(value)
    return answer