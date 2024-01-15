# day 4 복습
# 1 - bfs (가장 빠른 거리)

import heapq
print("--------------------------------------------------")

h, w = map(int, input().split())
sh, sw = map(int, input().split())
eh, ew = map(int, input().split())

sh -= 1
sw -= 1
eh -= 1
ew -= 1

visit = [[0 for i in range(w)] for i in range(h)]

q = []
q.append([sh, sw])

visit[sh][sw] = 1

while q:
    i, j = q.pop(0)

    l = [0, 0, -1, 1]
    c = [-1, 1, 0, 0]

    for k in range(4):
        nl = i+l[k]
        nc = j+c[k]

        if 0 <= i < h and 0 <= j < w and visit[i][j] == 0:
            visit[nl][nc] = visit[i][j] + 1
            q.append([nl, nc])

print(visit[eh][ew]-1)


# 2 - bfs (미로탐험)

print("--------------------------------------------------")

h, w = map(int, input().split())
maze = []

for i in range(h):
    maze.append(input())

visit = [[0 for i in range(w)] for i in range(h)]

for i in range(h):
    for j in range(w):
        if maze[i][j] == '2':
            sh = i
            sw = j
            break

q = []
q.append([sh, sw])

visit[sh][sw] = 1

while q:
    i, j = q.pop(0)

    l = [0, 0, -1, 1]
    c = [-1, 1, 0, 0]

    for k in range(4):
        nl = i+l[k]
        nc = j + c[k]

        if 0 <= nl < h and 0 <= nc < w:
            if visit[nl][nc] == 0:
                if maze[nl][nc] == '1':
                    visit[nl][nc] = visit[i][j] + 1
                    q.append([nl, nc])

for i in range(h):
    for j in range(w):
        if maze[h][w] == '0':
            print(0, end=' ')
        else:
            print(visit[i][j]-1, end=' ')
    print()

# 3 - dfs&bfs (여행경로)

print("--------------------------------------------------")


def solution(tickets):
    answer = []
    tickets.sort()

    q = []
    q.append([['ICN'], tickets])

    while q:
        path, tic = q.pop(0)
        q.sort()

        if len(tic) == 0:
            answer = path
            break

        idx = -1

        for i in range(len(tic)):
            if path[-1] == tic[i][0]:
                idx = i
                break

        if idx == -1:
            continue

        while idx < len(tic) and tic[idx][0] == path[-1]:
            q.qppend([path+[tic[idx][1]], tic[:idx] + tic[idx+1:]])
            idx += 1

    return answer

# 4 - graph (가장 먼 노드)


print("--------------------------------------------------")


def solution2(n, edge):
    answer = 0
    visit = [0 for i in range(n+1)]
    li = [[]for i in range(n+1)]

    for i in range(len(edge)):
        li[edge[i][0]].append(edge[i][1])
        li[edge[i][1]].append(edge[i][0])

    q = []
    q.append(1)
    visit[1] = 1

    while q:
        i = q.pop(0)

        for j in li[i]:
            if visit[j] == 0:
                visit[j] = visit[i]+1
                q.append(j)
    answer = max(visit)
    answer = visit.count(answer)

    return answer

# 5 - graph (전력망을 둘로 나누기)


print("--------------------------------------------------")


def bfs(cut, graph, n):
    visit = [0 for i in range(n)]

    n = 1

    visit[cut[0]] = 1
    visit[cut[1]] = 1

    q = []
    q.append(cut[0])

    while q:
        i = q.pop(0)
        for j in graph[i]:
            if visit[j] == 0:
                n += 1
                visit[j] = n
                q.append(j)
    return n


def solution3(n, wires):
    answer = n

    graph = [[] for i in range(n+1)]

    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)

    for i in wires:
        cnt = bfs(i, graph, n)

        answer = min(answer, abs(cnt-(n-cnt)))

    return answer


# 5 - heap (더 맵게)
print("--------------------------------------------------")


def solution4(s, k):
    answer = 0
    he = []
    s.sort()
    for i in s:
        heapq.heappush(he, i)

    while he[0] < k:
        heapq.heappush(he, heapq.heappop(he) + heapq.heappop(he)*2)
        answer += 1
        if len(he) == 1 and he[0] < k:
            return -1

    return answer


# 6 - dp (피보나치 수)
print("--------------------------------------------------")


def solution5(n):
    answer = 0
    li = [0, 1]
    for i in range(2, n+1):
        li.append((li[i-2]+li[i-1] % 1234567))

    answer = li[-1]
    return answer
