# 진료 순서 정하기
def solution(emergency):
    answer = []
    arr = [x for x in emergency]
    arr.sort(reverse=True)
    for i in emergency:
        if i in arr:
            answer.append((arr.index(i))+1)
    return answer
