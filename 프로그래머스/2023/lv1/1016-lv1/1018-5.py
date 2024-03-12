# 크기가 작은 부분문자열
def solution(t, p):
    answer = ""
    res = 0
    t = [x for x in str(t)]
    for i in range(len(t)-len(p)+1):
        for j in range(len(p)):
            answer += t[i+j]
        if int(answer) <= int(p):
            res += 1
            answer = ""
        else:
            answer = ""

    return res
