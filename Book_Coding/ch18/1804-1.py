# 두 수의 합 2 - 투 포인터
'''
정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
*주의: 이 문제에서 배열은 0 아닌 1부터 시작하는 것으로 함
'''
from typing import List


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers)-1
    while not left == right:
        if numbers[left]+numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            return left+1, right+1  # 리턴 값 + 1
