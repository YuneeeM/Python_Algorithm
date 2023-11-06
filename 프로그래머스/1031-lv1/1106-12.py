#[1차] 다트 게임
def solution(dartResult):
    res = ''
    answer = []
    for x in dartResult:
        if x.isnumeric():
            res += x
        elif x == 'S':
            res = int(res)**1
            answer.append(res)
            res = ''
        elif x == 'D':
            res = int(res)**2
            answer.append(res)
            res = ''
        elif x == 'T':
            res = int(res)**3
            answer.append(res)
            res = ''
        elif x == '*':
            if len(answer) > 1:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif x == '#':
            answer[-1] = answer[-1] * -1
        
    return sum(answer)