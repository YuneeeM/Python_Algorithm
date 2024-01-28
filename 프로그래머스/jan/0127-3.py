#숫자 짝꿍

def solution(X, Y):
    answer = ''
    cntX = [0 for i in range(10)]
    cntY = [0 for i in range(10)]
    
    for i in str(X):
        cntX[int(i)] += 1
    for j in str(Y):
        cntY[int(j)] += 1
    
    for i in range(0, 10):
        if cntX[i] > 0 and cntY[i] > 0:
            answer += str(i) * min(cntX[i], cntY[i])

    if not answer:
        return "-1"

    answer_list = list(answer)
    answer_list.sort(reverse=True)
    
    if answer_list[0] == "0":
        return "0"
    
    return ''.join(answer_list)