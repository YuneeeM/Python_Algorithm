# 재귀를 사용하는 이유

# 동전 앞 0, 뒤 1
# 동전이 3개일 때 나올 수 있는 모든 경우의 수
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(i, j, k)

# n이 10이라면--> 굉장히 비효율적이다!
# 재귀함수란 내가 깊이를 자유롭게 지정할 수 있는 것!(깊이있게 들어가기!)

i = 0

# 5까지만 출력
while True:
    # 끝나는 조건
    if i == 5+1:
        break
    print(i)
    i += 1

print("----------------------------")


def f(n):
    if n == 0:
        return
    print(n)
    f(n-1)


f(5)

print("----------------------------")


def num(N):
    if N == 0:
        return
    num(N-1)
    print(N)


n = int(input())
num(n)
