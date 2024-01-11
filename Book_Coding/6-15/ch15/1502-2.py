# 배열의 k번째 큰 요소 - heapq 모듈의 heapify 이용
'''
정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.
'''

import heapq
from typing import List


def findKthLargest(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)

    for _ in range(len(nums)-k):
        heapq.heappop(nums)

    return heapq.heappop(nums)
