import sys
from collections import deque

sys.stdin = open("0808/input4.txt", "rt")  # 파일 읽어오기

'''
합이 같은 부분집합(DFS)

n개의 원소로 구성된 자연수 집합이 주어지면,
이 집합을 두개의 부분집합으로 나누었을 때 
두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 "YES"를 출력하고,
그렇지 않으면 "NO" 출력함
예를 들어 {1, 3, 5, 6, 7, 10}이 입력되면 {1, 3, 5, 7} = {6, 10} 으로 두 부분집합의 합이 
16으로 같은 경우가 존재하는 것을 알 수 있다.
'''


def DFS(L, sum):
    if sum > total//2:
        return
    if L == n:
        if sum == (total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")
