# 네트워크 딜레이 타임 - 다익스트라 알고리즘 구현
'''
k부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라.
불가능할 경우 -1을 리턴한다. 입력값 (u,v,w)는 각각 출발지, 도착지, 소요 시간으로 구성되며,
전체 노드의 개수는 N으로 입력받는다.
'''

'''
파이썬 heapq 모듈은 priority queue 알고리즘을 제공함
모든 부모 노드는 그의 자식 노드보다 값이 작거나 큰 이진트리 구조인데, 내부적으로는 인덱스 0에서 시작해 
k번째 원소가 항상 자식 원소들 (2k+1, 2k+2) 보다 작거나 같은 최소 힙의 형태로 정렬됨

*힙 함수
heapq.heappush(heap,item)
: item을 heap에 추가

heapq.heappop(heap)
: 가장 작은 원소를 pop & 리턴, 비어 있는 경우 indexerror가 호출됨

heapq.heapify(x)
: 리스트 x를 즉각적으로 heap으로 변환함 (in linear time = O(N))
'''




import collections
import heapq
from typing import List
def networkDelayTime(self, times: List[List[int]], N : int, K : int) -> int:
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in times:
        graph[u].append((v, w))

    # 큐 변수 : [(소요시간, 정점)]
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time+w
                heapq.heappush(Q, (alt, v))

    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == N:
        return max(dist.values())

    return -1
