# 이진 검색 - 재귀 풀이

'''
이진 검색이란 정련된 배열에서 타겟을 찾는 검색 알고리즘
O(logN)

BST는 정렬된 구조를 저장하고 탐색하는 '자료구조'
이진검색은 정렬된 배열에서 값을 찾아내는 '알고리즘'

--정렬된 nums를 입력받아 이진 검색으로 target에 해당하는 인덱스를 찾아라.

'''

from typing import List


def search(self, nums: List[int], target: int) -> int:
    def binary_search(left, right):
        if left <= right:
            mid = (left+right) // 2

            if nums[mid] < target:
                return binary_search(mid+1, target)
            elif nums[mid] > target:
                return binary_search(left, mid-1)
            else:
                return mid
        else:
            return -1

    return binary_search(0, len(nums)-1)
