# 원점에 k번째로 가까운 점
'''
평면상에 points 목록이 있을 때, 원점 (0,0)에서 k번 가까운 점 목록을 순서대로 출력하라.
평면상 두 점의 거리는 유클리드 거리로 한다.
'''
import heapq
from typing import List


def KClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    heap = []
    for (x, y) in points:
        dist = x**2+y**2
        heapq.heappush(heap, (dist, x, y))

    result = []
    for _ in range(K):
        (dist, x, y) = heapq.heappop(heap)
        result.append((x, y))

    return result
