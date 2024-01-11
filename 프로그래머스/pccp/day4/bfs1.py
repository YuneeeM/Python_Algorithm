# bfs - 가장 빠른 거리
'''
일할 것들을 뒤에 그냥 보내버리고, ->bfs
visit를 사용해야한다.
'''

h, w = map(int, input().split())
sh, sw = map(int, input().split())
eh, ew = map(int, input().split())

sh -= 1
sw -= 1
eh -= 1
ew -= 1

visit = [[0 for i in range(w)] for i in range(h)]

visit[sh][sw] = 1

q = []
q.append([sh, sw])

while q:
    i, j = q.pop(0)

    l = [0, 0, -1, 1]
    c = [-1, 1, 0, 0]

    for k in range(4):
        nl = i+l[k]
        nc = j+c[k]
        if 0 <= nl < h and 0 <= nc < w and visit[nl][nc] == 0:
            visit[nl][nc] = visit[i][j] + 1
            q.append([nl, nc])

print(visit[eh][ew]-1)
