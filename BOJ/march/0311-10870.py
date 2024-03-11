# 피보나치 수 5 - 재귀
n = int(input())


def f(n):
    if n <= 1:
        return n
    return f(n-1) + f(n-2)


print(f(n))
