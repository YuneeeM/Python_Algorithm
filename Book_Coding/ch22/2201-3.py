# 과반수 엘리먼트 - 분할정복
'''
과반수를 차지하는(절반을 초과하는) 엘리먼트를 출력하라 
'''

from typing import List

def majorityElement(self,nums:List[int]) -> int:
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    
    half = len(nums)//2
    a=self.majorityElement(nums[:half])
    b=self.majorityElement(nums[half:])

    return [b,a][nums.count(a)>half]