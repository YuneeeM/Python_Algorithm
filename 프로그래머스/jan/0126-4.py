#올바른 괄호

import collections
def solution(s):
    answer = []
    s = list(s)
    s = collections.deque(s)
    
    while s:
        cur = s.popleft()
        
        if cur == '(':
            answer.append(cur)
        else:
            if len(answer) == 0:
                return False
            elif answer[-1] == '(':
                answer.pop()
    
    if answer:
        return False
    else:
        return True
    