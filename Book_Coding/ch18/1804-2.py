# 두 수의 합 2 - 이진 검색
'''
정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
*주의: 이 문제에서 배열은 0 아닌 1부터 시작하는 것으로 함
'''
from typing import List


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    for k, v in enumerate(numbers):
        left, right = k+1, len(numbers)-1
        expected = target-v
        # 이진 검색으로 나머지 값 판별
        while left <= right:
            mid = left + (right-left)//2
            if numbers[mid] < expected:
                left = mid+1
            elif numbers[mid] > expected:
                right = mid-1
            else:
                return k+1, mid+1
