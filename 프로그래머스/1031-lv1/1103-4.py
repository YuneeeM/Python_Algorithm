#과일 장수
def solution(k, m, score):
    answer = 0
    arr=[]
    res=[]
    
    score.sort(reverse=True)
    
    for i in range(0,len(score),m):
        for j in range(m):
            if i+j < len(score):
                arr.append(score[i+j])
        if len(arr) == m:
            res.append(arr)
            arr=[]
        
    
    for i in range(len(res)):
        answer+=min(res[i])*m
    return answer

