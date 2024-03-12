# 약수의 개수와 덧셈
def num(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
    return cnt


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if num(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
