# 과반수 엘리먼트 - 파이썬다운 방식
'''
과반수를 차지하는(절반을 초과하는) 엘리먼트를 출력하라 
'''

from typing import List

def majorityElement(self,nums:List[int]) -> int:
    return sorted(nums)[len(nums)//2]