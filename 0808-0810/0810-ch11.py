import sys

sys.stdin = open("0808/input11.txt", "rt")  # 파일 읽어오기

'''
수들의 조합
n개의 정수가 주어지면 그 숫자들 중 k개를 뽑는 조합의 합이 임의의 정수 m의 배수인 개수는 
몇 개가 있는 지 출력하는 프로그램
'''


def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+a[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
