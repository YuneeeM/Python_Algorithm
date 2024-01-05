# 배열의 k번째 큰 요소 - 정렬을 이용한 풀이
'''
정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.
'''
from typing import List


def findKthLargest(self, nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[k-1]
