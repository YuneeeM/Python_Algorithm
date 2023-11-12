# 외계어 사전
def solution(spell, dic):
    answer = 0
    n = len(spell)
    arr = []
    for x in dic:
        answer = 0
        for i in spell:
            if i in x:
                answer += 1
        arr.append(int(answer))

    for x in arr:
        if x == n:
            return 1
    else:
        return 2
