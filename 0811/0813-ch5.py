import sys

sys.stdin = open("0811/input5.txt", "rt")  # 파일 읽어오기

'''
동전 분배하기(DFS)

n개의 동전을 a,b,c 세명에게 나누어주려고 함
총액이 가장 큰 사람과 가장 작은 사람의 최소차를 출력
'''


def DFS(L):
    global res
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]


if __name__ == "__main__":
    n = int(input())
    coin = []
    money = [0]*3
    res = 2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)
