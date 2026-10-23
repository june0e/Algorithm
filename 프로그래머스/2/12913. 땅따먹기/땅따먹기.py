def solution(land):
    answer = 0
    
    dp = [land[0][:]]
    for low in range(1,len(land)): #행만큼 반복
        current_low = []
        
        for col in range(4): #열의 개수는 4개
            best = 0
            
            for prev_col in range(4):  # 이전 행에서 밟았던 열 후보
                if prev_col != col:  # 같은 열만 제외
                    best = max(best, dp[-1][prev_col]) #직전열에서 max값 
            
            current_low.append(land[low][col]+best)

        dp.append(current_low)
    return max(dp[-1])