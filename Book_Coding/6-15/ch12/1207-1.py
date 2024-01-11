#일정 재구성 - DFS로 일정 그래프 구성
'''
[from, to]로 구성된 항공권 목록을 이용해 JFK에 출발하는 여행 일정을 구성하라.
여러 일정이 있는 경우 사전 어휘순으로 방문한다.
'''
import collections
from typing import List

def findItinerary(self, tickets: List[List[str]]) -> List[str]:
  graph = collections.defaultdict(list)
  #그래프 순서대로 구성
  for a,b in sorted(tickets):
    graph[a].append(b)
  
  route = []
  def dfs(a):
    #첫 번째 값을 읽어 어휘 순 방문
    while graph[a]:
      dfs(graph[a].pop(0))
    route.append(a)

  dfs('JFK')

  #다시 뒤집어 어휘 순 결과로
  return route[::-1]
