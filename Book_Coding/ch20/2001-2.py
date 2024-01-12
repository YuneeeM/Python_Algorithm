# 최대 슬라이싱 윈도우 - 큐를 이용한 최적화
'''
배열 nums가 주어졌을 때 k 크기의 슬라이딩 윈도우를 오른쪽 끝까지
이동하면서 최대 슬라이딩 윈도우를 구하라
'''
from typing import List
import collections


def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    results = []
    window = collections.deque()
    current_max = float('-inf')
    for i, v in enumerate(nums):
        window.append(v)
        if i < k-1:
            continue

        # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        results.append(current_max)

        # 최댓값이 윈도우에서 빠지면 초기화
        if current_max == window.popleft():
            current_max = float('-inf')

    return results
