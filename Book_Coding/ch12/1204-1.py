#조합 - DFS로 k개 조합 생성
'''
전체 수 n을 입력받아 k개의 조합을 리턴한다.
'''
from typing import List


def combine(self, n:int, k:int) -> List[List[int]]:
  results=[]

  def dfs(elements, start:int, k:int):
    if k==0:
      results.append(elements[:])
      return
    
    #자신 이전의 모든 값을 고정하여 재귀 호출
    for i in range(start,n+1):
      elements.append(i)
      dfs(elements,i+1,k-1)
      elements.pop()
  dfs([],1,k)
  return results