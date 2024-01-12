# 최대 슬라이싱 윈도우 - 브루트 포스로 계산
'''
배열 nums가 주어졌을 때 k 크기의 슬라이딩 윈도우를 오른쪽 끝까지
이동하면서 최대 슬라이딩 윈도우를 구하라
'''
from typing import List


def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    if not nums:
        return nums

    r = []
    for i in range(len(nums)-k+1):
        r.append(max(nums[i:i+k]))
