# 소인수분해
def isPrime(x):
    if x == 2 or x == 3:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(n):
    answer = []
    for i in range(2, n+1):
        if n % i == 0 and isPrime(i) == True:
            n = n//i
            answer.append(i)
    return answer
