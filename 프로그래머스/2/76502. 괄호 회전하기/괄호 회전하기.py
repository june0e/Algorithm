from collections import deque
def solution(s):
    s = deque(s)
    answer = 0 
    
    
    for i in range(len(s)):
        open = []
        valid = True
        for j in s:
            if j == '[' or j == '{' or j == '(':
                open.append(j)
            else:
                if j == ']' and open and open[-1] == '[' :
                    open.pop()
                    continue
                elif j == '}' and open and open[-1] == '{':
                    open.pop()
                    continue
                elif j == ')' and open and open[-1] == '(':
                    open.pop()
                    continue
                else :
                    valid = False
                    break
        if valid and len(open) == 0:
            answer+=1
        x = s.popleft()
        s.append(x)
        
    return answer