# 분수의 덧셈
def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


def solution(numer1, denom1, numer2, denom2):
    answer = []

    a = numer1*denom2+numer2*denom1
    b = denom1*denom2

    res = gcd(b, a)

    answer = [a/res, b/res]

    return answer
