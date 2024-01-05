# 배열의 k번째 큰 요소 - heapq 모듈 이용
'''
정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.
'''

import heapq
from typing import List


def findKthLargest(self, nums: List[int], k: int) -> int:
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)

    for _ in range(1, k):
        heapq.heappop(heap)

    return -heapq.heappop(heap)
