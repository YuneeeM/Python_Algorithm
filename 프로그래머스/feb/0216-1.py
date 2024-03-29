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