#기사단원의 무기
def isPrime(x):
        cnt = 0
        for i in range(1, int(x**0.5) + 1):
            if x % i == 0:
                if i == (x // i):
                    cnt += 1
                else:
                    cnt += 2
        return cnt


def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        w_power = isPrime(i)
        if w_power > limit:
            answer += power
        else:
            answer += w_power
            
    return answer