#순열 - itertools 모듈 사용
'''
서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.
'''

import itertools
from typing import List


def permute(self,nums:List[int]) -> List[List[int]]:
  return list(itertools.permute(nums))