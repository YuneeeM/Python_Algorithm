# 피보나치 수 - 다이나믹 프로그래밍 (동적 계획법)

'''
- 하나의 큰 문제를 여러 개의 작은 규칙적인 문제로 나누어서 해결 = 점화식을 사용할 수 있는가
- 작은 문제로 나누었을 때 중복되는 부분을 저장하여 다시 저장 = 데이터 재활용
'''


def solution(n):
    answer = 0
    li = [0, 1]
    for i in range(2, n+1):
        li.append((li[i-2]+li[i-1]) % 1234567)
    answer = li[n]
    return answer


print("------------파이썬의 한계---------------")


def solution2(n):
    answer = 0
    memo = [0 for i in range(n+1)]

    def f(n):
        # 계산한 적이 있나요?
        if memo[n] != 0:
            return memo[n]
        if n <= 2:
            memo[n] = 1
            return memo[n]
        memo[n] = (f(n-2) + f(n-1)) % 1234567
        return memo[n]

    answer = f(n)
    return answer
