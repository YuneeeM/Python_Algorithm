# 과반수 엘리먼트 - 브루트 포스로 과반수 비교
'''
과반수를 차지하는(절반을 초과하는) 엘리먼트를 출력하라 
'''

from typing import List


def majorityElement(self, nums:List[int]) -> int:
    for num in nums:
        if nums.count(num) > len(nums)//2:
            return num