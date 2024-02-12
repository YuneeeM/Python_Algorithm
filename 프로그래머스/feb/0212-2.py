# 타겟 넘버 (BFS)

def solution(numbers, target):
    res=[0]
    answer = 0
    
    for num in numbers:
        temp=[]
        
        for leaf in res:
            temp.append(leaf+num)
            temp.append(leaf-num)
        res = temp
    
    for leaf in res:
        if leaf == target:
            answer+=1
    return answer