import sys
from collections import deque
sys.stdin = open("0811/input7.txt", "rt")  # 파일 읽어오기

'''
송아지 찾기(BFS: 상태트리탐색)
현수의 위치와 송아지의 위치가 직선상의 좌표 점으로 주어지면 현수는 현재 위치에서 송아지의 위치까지 이동
한번 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동가능 최소 몇 번 점프
'''


MAX = 10000
ch = [0]*(MAX+1)
dis = [0]*(MAX+1)
n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    if next == m:
        break
    for next in (now-1, now+1, now+5):
        if 0 < next <= MAX:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now]+1
print(dis[m])
