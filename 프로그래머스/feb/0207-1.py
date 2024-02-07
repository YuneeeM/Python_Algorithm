#n의 배수
def solution(num, n):
    return int(not(num % n))

#[PCCE 기출문제] 10번 / 데이터 분석
def solution(data, ext, val_ext, sort_by):
    answer = []

    for i in data:
            if ext == "code" and val_ext > i[0] :
                answer.append(i)
            elif ext == "date" and val_ext > i[1]:
                answer.append(i)
            elif ext == "maximum" and val_ext > i[2] :
                answer.append(i)
            elif ext == "remain" and val_ext > i[3] :
                answer.append(i)

    if sort_by == 'code':
        answer.sort(key=lambda x: x[0])
    elif sort_by == 'date':
        answer.sort(key=lambda x: x[1])
    elif sort_by == 'maximum':
        answer.sort(key=lambda x: x[2])
    elif sort_by == 'remain':
        answer.sort(key=lambda x: x[3])

    return answer