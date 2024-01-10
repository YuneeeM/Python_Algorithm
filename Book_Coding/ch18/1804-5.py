# 두 수의 합 2 - bisect 모듈 + 슬라이싱 제거
'''
정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
*주의: 이 문제에서 배열은 0 아닌 1부터 시작하는 것으로 함
'''
from typing import List
import bisect


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    for k, v in enumerate(numbers):
        expected = target-v
        i = bisect.bisect_left(numbers, expected, k+1)
        if i < len(numbers) and numbers[i] == expected:
            return k+1, i+1
