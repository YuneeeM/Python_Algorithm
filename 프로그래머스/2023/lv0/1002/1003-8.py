# 다항식 더하기
def solution(polynomial):
    answer = [0, 0]
    polynomial = polynomial.split('+')
    for x in polynomial:
        x = x.strip()
        if x[-1] == 'x':
            xx = x[:-1]
            if xx:
                answer[0] += int(xx)
            else:
                answer[0] += 1
        else:
            answer[1] += int(x)
    res = []
    if answer[0]:
        if answer[0] == 1:
            res.append('x')
        else:
            res.append(f'{answer[0]}x')
    if answer[1]:
        res.append(f'{answer[1]}')
    return ' + '.join(res)
