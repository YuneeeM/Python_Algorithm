# 숫자만들기

def f(maxnum, num):
    # 끝내는 조건
    # limit 보다 크면 동작하지 않음
    if N < num:
        return maxnum
    # 가장 큰값 다시 저장하기(갱신)?
    maxnum = max(maxnum, num)
    # 재귀함수 시작
    for i in range(K):
        maxnum = f(maxnum, num*10+Q[i])
    return maxnum


N, K = map(int, input().split())
Q = list(map(int, input().split()))
print(f(0, 0))
