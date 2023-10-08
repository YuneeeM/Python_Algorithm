# 등수 매기기

def solution(score):
    answer = []
    res = []

    for x in score:
        res.append(sum(x)/len(x))

    arr = sorted(res, reverse=True)

    for x in res:
        answer.append(arr.index(x)+1)

    return answer
