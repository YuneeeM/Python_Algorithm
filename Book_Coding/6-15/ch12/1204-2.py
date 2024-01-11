#조합 - itertools 모듈 사용
'''
전체 수 n을 입력받아 k개의 조합을 리턴한다.
'''
import itertools
from typing import List

def combine(self, n:int, k:int) -> List[List[int]]:
  return list(itertools.combinations(range(1,n+1),k))