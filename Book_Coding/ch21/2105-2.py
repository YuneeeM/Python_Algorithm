# 주유소 - 모두방문
'''
원형으로 경로가 연결된 주유소 목록이 있다. 각 주유소는 gas[i] 만큼의 기름을 갖고 있으며
다음 주유소로 이동하는데 cost[i]가 필요하다. 기름이 부족하면 이동할 수 없다고 할 때 모든 주유소를 
방문할 수 있는 출발점의 인덱스를 출력하라.

출발점이 존재하지 않을 경우 -1을 리턴하며, 출발점은 유일하다.
'''
def canCompleteCircuit(self, gas:List[int], cost:List[int]) -> int:
  for start in range(len(gas)):
    fuel=0
    for i in range(start,len(gas)+start):
      index=i%len(gas)

      can_travel = True
      if gas[index] +fuel < cost[index]:
        can_t