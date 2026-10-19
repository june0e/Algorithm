def solution(nums):
    answer = 0
    counts ={}
    value = []
    for phoneketmon in nums:
        counts[phoneketmon] = counts.get(phoneketmon,0)+1
    
    
    return min(len(counts), len(nums) // 2)