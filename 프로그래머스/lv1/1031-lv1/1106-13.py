#로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    answer = []
    zero=0
    num=0
    for x in lottos:
        if x == 0:
            zero+=1
        if x in win_nums:
            num+=1
            
    if num+zero == 6:
        answer.append(1)
    elif num+zero == 5:
        answer.append(2)
    elif num+zero == 4:
        answer.append(3)
    elif num+zero == 3:
        answer.append(4)
    elif num+zero == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    if num == 6:
        answer.append(1)
    elif num == 5:
        answer.append(2)
    elif num == 4:
        answer.append(3)
    elif num == 3:
        answer.append(4)
    elif num == 2:
        answer.append(5)
    else:
        answer.append(6)
        
   
    return answer