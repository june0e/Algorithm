from collections import deque
def solution(prices):
    answer = []
    prices_all = deque(prices)
    result = 0
    while (prices_all):
        price = prices_all.popleft()

        for idx,x in enumerate(prices_all):
            if price > x:
                result += 1
                break
            else : result += 1
        answer.append(result)
        result = 0
        
    return answer