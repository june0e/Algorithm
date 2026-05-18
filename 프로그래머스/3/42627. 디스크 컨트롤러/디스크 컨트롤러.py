import heapq
def solution(jobs):
    answer = 0
    waiting = []
    jobs.sort()
    current_time = 0
    idx = 0
    while idx < len(jobs) or waiting:
        while idx < len(jobs) and jobs[idx][0] <= current_time:
            x, y = jobs[idx]
            heapq.heappush(waiting, (y, x))
            idx += 1
        if waiting:
            x, y = heapq.heappop(waiting)
            current_time += x
            answer += current_time - y
        else:
            current_time = jobs[idx][0]
    answer = answer // len(jobs)
    return answer