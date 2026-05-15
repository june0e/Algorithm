from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    bridge = deque([0] * bridge_length, maxlen = bridge_length) 
    trucks = deque(truck_weights)
    current_weight = 0
    answer = 0
    
    while trucks or current_weight > 0 :
        answer += 1
        out = bridge.popleft()
        current_weight -= out
        
        if trucks and current_weight + trucks[0] <= weight:
            bridge.append(trucks[0])
            current_weight += trucks[0]
            trucks.popleft()
        else:
            bridge.append(0)

    return answer