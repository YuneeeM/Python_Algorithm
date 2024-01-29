#과일 장수

def solution(k, m, score):
    answer = 0
    score.sort()
    while score:
        temp=[]
        for _ in range(m):
            if score:
                temp.append(score.pop())
            else:
                temp=[]
        if temp:
            answer+=min(temp)*m
    return answer


# 똑똑한 풀이
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m