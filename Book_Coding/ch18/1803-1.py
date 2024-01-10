# 두 배열의 교집합 - 브루트 포스로 계산
'''
두 배열의 교집합을 구하라
'''

from typing import List


def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result: set = set()
    for n1 in nums1:
        for n2 in nums2:
            if n1 == n2:
                result.add(n1)

    return result
