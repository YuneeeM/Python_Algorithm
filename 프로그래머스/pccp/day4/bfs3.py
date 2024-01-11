# 여행경로
import collections


def solution(tickets):
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)

    answer = []

    def dfs(a):

        while graph[a]:
            dfs(graph[a].pop(0))
        answer.append(a)

    dfs("ICN")
    return answer[::-1]


print("--------------------------")


def solution2(tickets):
    answer = []
    # 출발지, 목적지 기준 정렬

    tickets.sort()  # 자동으로 처음, 두번째 세번째... 순서로 오름차순 정렬

    # 앞부분은 내가 거쳐온 경로, 남아 있는 티켓 / 정렬
    q = []
    q.append([["ICN"], tickets])

    while q:
        path, tic = q.pop(0)
        q.sort()

        print(path, tic)

        # 남은 티켓이 없다면 끝
        if len(tic) == 0:
            answer = path
            break

        idx = -1
        # 현제 출발 공항이 있는 티켓의 위치 찾기
        for i in range(len(tic)):
            if path[-1] == tic[i][0]:
                idx = i
                break

        # 만약 찾지 못한다면
        if idx == -1:
            continue

        # 전체 티켓을 찾으면서 큐에다 넣어줘
        while idx < len(tic) and tic[idx][0] == path[-1]:
            q.append([path + [tic[idx][1]], tic[:idx] + tic[idx+1:]])
            idx += 1

    return answer
