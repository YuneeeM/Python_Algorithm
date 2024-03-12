# 배달
from collections import defaultdict, deque


def solution(N, road, K):
    answer = 0

    graph = defaultdict(list)

    for i, j, dis in road:
        graph[i].append([j, dis])
        graph[j].append([i, dis])

    q = []
    q = deque(q)
    q.append([1, 0])

    visit = [0 for i in range(N+1)]

    visit[1] = 1

    while q:
        node, dis = q.popleft()

        for v, w in graph[node]:
            if dis + w <= K and (not visit[v] or dis + w <= visit[v]):
                q.append([v, dis+w])
                visit[v] = dis+w

    answer = N+1 - visit.count(0)

    return answer
