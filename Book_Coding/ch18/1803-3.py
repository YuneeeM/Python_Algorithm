# 두 배열의 교집합 - 투 포인터로 일치 여부 판별
'''
두 배열의 교집합을 구하라
'''

from typing import List


def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result: set = set()
    # 양쪽 모두 정렬
    nums1.sort()
    nums2.sort()
    i = j = 0
    # 투 포인터 우측으로 이동하며 일치 여부 판별
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1
    return result
