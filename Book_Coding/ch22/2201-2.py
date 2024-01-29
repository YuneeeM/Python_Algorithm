# 과반수 엘리먼트 - 다이나믹 프로그래밍
'''
과반수를 차지하는(절반을 초과하는) 엘리먼트를 출력하라 
'''

from typing import List
import collections

def majorityElement(self,nums:List[int]) -> int:
    counts = collections.defaultdict(int)
    for num in nums:
        if counts[num] == 0:
            counts[num]=nums.count(num)

        if counts[num] > len(nums)//2:
            return num