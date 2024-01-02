#부분집합 - 트리의 모든 DFS 결과
'''
모든 부분 집합을 리턴하라.
'''
from typing import List


def subsets(self, nums: List[int]) -> List[List[int]]:
  result=[]

  def dfs(index, path):
    #매번 결과 추가
    result.append(path)

    #경로를 만들면서 DFS
    for i in range(index, len(nums)):
      dfs(i+1, path+[nums[i]])
    
  dfs(0,[])
  return result
  

  