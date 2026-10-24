def solution(sequence, k):
    #K는 부분수열의 합 
    #sequence 는 오름차준으로 정렬된 수열
    answer = []
    
    left = 0
    right = 0 
    
    current_sum = 0
    best_len = float('inf') #무한대
    best_str_idx, best_end_idx = 0,0
    cnt = []
    
    for i in sequence:
        # 1. sum에 i 더하기
        current_sum += i
        right+=1
        if current_sum > k:
            while current_sum > k:
                current_sum -= sequence[left]
                left+=1
                
        if current_sum == k:
            current_len = right-left
            if current_len < best_len or(current_len == best_len and left < best_str_idx) :
                best_len = right - left
                best_str_idx = left
                best_end_idx = right-1
    
    answer.append(best_str_idx)
    answer.append(best_end_idx)
    
    return answer