import heapq
def solution(scoville, K):
    heapq.heapify(scoville) # 정렬을 heapq로 변경
    answer = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            answer = -1
            return answer
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = first + second * 2
        heapq.heappush(scoville,mixed)
        answer+=1
    return answer