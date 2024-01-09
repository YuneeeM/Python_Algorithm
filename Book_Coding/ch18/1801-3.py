# 이진 검색 - 이진 검색 모듈

'''
정렬된 nums를 입력받아 이진 검색으로 target에 해당하는 인덱스를 찾아라.

'''

from typing import List
import bisect


def search(self, nums: List[int], target: int) -> int:
    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1
