# 타겟 넘버

def dfs(numbers,target,L,psum):
    global answer
   
    
    if L == len(numbers) and psum == target:
        answer+=1
        return
    
    elif L == len(numbers):
        return
    
    dfs(numbers,target,L+1, psum+numbers[L])
    dfs(numbers,target,L+1, psum-numbers[L])

def solution(numbers, target):
    
    global answer
    answer=0
    dfs(numbers, target, 0, 0)
    
    return answer