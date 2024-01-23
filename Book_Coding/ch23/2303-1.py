# 최대 서브 배열 - 메모이제이션
from typing import List


def maxSubArray(self,nums:List[int]) -> int:
    for i in range(1,len(nums)):
        nums[i] += nums[i-1] if nums[i-1] > 0 else 0
    return max(nums)
    