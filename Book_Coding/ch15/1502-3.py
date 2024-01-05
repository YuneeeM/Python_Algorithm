# 배열의 k번째 큰 요소 - heapq 모듈의 nlargest 이용
'''
정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.
'''

import heapq
from typing import List


def findKthLargest(self, nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]
