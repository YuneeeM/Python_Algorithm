#덧칠하기
def solution(n, m, section):
    answer = 0
    paint = 0
    
    for s in section:
        if paint <= s:
            paint = s+m
            answer+=1
    
    return answer