import sys
from collections import deque
sys.stdin = open("0826/input14.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)

'''
회장뽑기(플로이드-워샬 응용)
각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받게 된다. 
예를 들어 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다. 어느 회원의 
점수가 2점이면, 다른 모든 회원이 친구이거나, 친구의 친구임을 말한다. 또한, 어느 회원의 
점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친국의 친구의 친구임을 
말한다.4점, 5점등은 같은 방법으로 정해진다. 
각 회원의 점수를 정할 때 주의할 점은 어떤 두 회원이 친구 사이이면서 동시에 친구의 친구
사이이면, 이 두 사람은 친구사이라고 본다. 회장은 회원들 중에서 점수가 가장 작은 사람이 
된다. 
회장의 점수와 회장이 될 수 있는 모든 사람을 찾는 프로그램을 작성하시오
'''

n = int(input())
dis = [[100]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dis[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dis[a][b] = 1
    dis[b][a] = 1
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])
res = [0]*(n+1)
score = 100
for i in range(1, n+1):
    for j in range(1, n+1):
        res[i] = max(res[i], dis[i][j])
    score = min(score, res[i])
out = []
for i in range(1, n+1):
    if res[i] == score:
        out.append(i)
print("%d %d" % (score, len(out)))
for x in out:
    print(x, end=' ')
