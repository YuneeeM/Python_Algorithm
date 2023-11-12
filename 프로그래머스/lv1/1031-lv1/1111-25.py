#성격 유형 검사하기
def solution(survey, choices):
    answer = ''
    res= {"R" : 0,"T" : 0,"C" : 0,"F" : 0,"J" : 0,"M" : 0,"A" : 0,"N" : 0 }
    
    for key,val in zip(survey,choices):
        if val>4:     
            res[key[1]] += val-4
        else: 
            res[key[0]] += 4-val
    
    arr = list(res.items())
    
    for i in range(0,8,2):
        if arr[i][1] < arr[i+1][1]:
            answer += arr[i+1][0]
        else:   
            answer += arr[i][0]
        
    return answer