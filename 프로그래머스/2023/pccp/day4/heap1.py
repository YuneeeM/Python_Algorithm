# 더 맵게
import heapq


def solution(s, K):
    answer = 0
    he = []
    s.sort()
    for i in s:
        heapq.heappush(he, i)

    while he[0] < K:
        heapq.heappush(he, heapq.heappop(he)+heapq.heappop(he) * 2)
        answer += 1
        if len(he) == 1 and he[0] < K:
            return -1

    return answer
