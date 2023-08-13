import sys

sys.stdin = open("0811/input3.txt", "rt")  # 파일 읽어오기

'''
양팔저울(DFS)
무게가 서로 다른 k개의 추와 빈 그릇이 있음
양팔 저울을 한 번만 이용하여 원하는 물의 무게를 그릇에 담고자 함
주어진 모든 추 무게의 합을 s라 하자, 예를 들어 추가 3개이고, 각 추의 무게가 {1,2,6}
이면 s=9임
'''


def DFS(L, sum):
    global res
    if L == n:
        if 0 < sum <= s:  # 양수만 체크(음수와 대칭구조)
            res.add(sum)

    else:
        DFS(L+1, sum+G[L])
        DFS(L+1, sum-G[L])
        DFS(L+1, sum)


if __name__ == "__main__":
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set()
    DFS(0, 0)
    print(s-len(res))
