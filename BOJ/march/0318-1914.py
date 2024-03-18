# 하노이 탑 - 임의 정밀도/큰 수 연산

def hanoi(n, a, b, c):
    if (n == 1):
        print(a, c)
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)


n = int(input())
print(2**n-1)
if (n <= 20):
    hanoi(n, 1, 2, 3)
