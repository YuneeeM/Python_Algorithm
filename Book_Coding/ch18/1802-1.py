# 회전 정렬된 배열 검색 - 피벗을 기준으로 한 이진 검색
'''
특정 피벗을 기준으로 회전하여 정렬된 배열에서 target값의 인덱스를 출력하라.
'''
from typing import List


def search(self, nums: List[int], target: int) -> int:
    # 예외처리
    if not nums:
        return -1

    # 최솟값을 찾아 피벗 설정
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left+(right-left)//2

        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid
    pivot = left

    # 피벗 기준 이진 검색
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right-left) // 2
        mid_pivot = (mid+pivot) % len(nums)

        if nums[mid_pivot] < target:
            left = mid+1
        elif nums[mid_pivot] > target:
            right = mid-1

        else:
            return mid_pivot
    return -1
