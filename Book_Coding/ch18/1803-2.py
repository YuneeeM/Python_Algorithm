# 두 배열의 교집합 - 이진 검색으로 일치 여부 판별
'''
두 배열의 교집합을 구하라
'''

from typing import List
import bisect


def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result: set = set()
    nums2.sort()
    for n1 in nums1:
        # 이진 검색으로 일치 여부 판별
        i2 = bisect.bisect_left(nums2, n1)
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)

    return result
