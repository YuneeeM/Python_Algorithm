# 이진 검색 - 반복 풀이

'''
정렬된 nums를 입력받아 이진 검색으로 target에 해당하는 인덱스를 찾아라.

'''

from typing import List


def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left+right)//2

        if nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid-1
        else:
            return mid
    return -1
