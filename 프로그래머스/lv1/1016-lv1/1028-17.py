# 추억 점수
def solution(name, yearning, photo):
    answer = []
    res = 0
    for i in range(len(photo)):
        for x in photo[i]:
            if x in name:
                res += yearning[name.index(x)]
        answer.append(res)
        res = 0
    return answer
