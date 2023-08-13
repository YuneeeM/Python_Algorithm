import sys

sys.stdin = open("0811/input4.txt", "rt")  # 파일 읽어오기

'''
동전 바꿔주기(DFS)

명보에게 T원의 지폐를 동전으로 바꿔주려고 함
입력으로 지폐의 금액 T, 동전의 가지수 k, 각 동전 하나의금액 pi와 개수 ni가 주어질 때
(i=1,2,...,k) 
지폐를 동전으로 교환하는 방법의 가지 수를 계산하는 프로그램을 작성하시오

'''


def DFS(L, sum):
    global cnt
    if sum > t:
        return
    if L == k:
        if sum == t:
            cnt += 1
    else:
        for i in range(ni[L]+1):
            DFS(L+1, sum+(pi[L]*i))


if __name__ == "__main__":
    t = int(input())
    k = int(input())
    pi = list()  # 동전 하나의 금액
    ni = list()  # 동전의 개수
    for i in range(k):
        a, b = map(int, input().split())
        pi.append(a)
        ni.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)
