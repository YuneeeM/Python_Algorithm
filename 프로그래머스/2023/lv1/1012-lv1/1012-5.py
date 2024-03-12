# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []

    if x < 0:
        end = x*n-1
    elif x == 0:
        answer = [0]*n
        return answer
    else:
        end = x*n+1

    for i in range(x, end, x):
        answer.append(i)

    return answer
