# 1부터 N까지의 합
def num(N):
    if N == 1:
        return 1

    return N + num(N-1)


n = int(input())
print(num(n))

print("--------------------------------")

# 바둑돌 배치하기
# 입력과 출력을 자유롭게 작성해주세요


def f(n, m):
    # 끝나는 조건
    if n % 2 == 0 or m % 2 == 0:
        return 0
    # 끝나지 않으면 반복되는 공식
    return 1+4*f(n//2, m//2)


n, m = map(int, input().split())
print(f(n, m))
