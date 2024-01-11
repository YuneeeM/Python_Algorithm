#조합의 합 - DFS로 중복 조합 그래프 탐색
'''
숫자 집합 candidates를 조합하여 합이 target이 되는 원소를 나열하라.
각 원소는 중복으로 나열 가능하다.
'''
from typing import List


def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
  result=[]

  def dfs(csum, index, path):
    #종료조건
    if csum < 0:
      return
    if csum == 0:
      result.append(path)
      return
    
    #자신 부터 하위 원소까지의 나열 재귀 호출
    for i in range(index, len(candidates)):
      dfs(csum-candidates[i], i ,path + [candidates[i]])

  dfs(target,0,[])
  return result