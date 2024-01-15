# 키에 따른 대기열 재구성
'''
여러명의 사람들이 줄을 서 있다. 각각의 사람은 (h,k)의 두 정수 쌍을 갖는데, h는 그 사람의 키,
k는 앞에 줄 서있는 사람들 중 자신의 키 이상인 사람들의 수를 뜻하낟.
이 값이 올바르도록 줄을 재정렬하는 알고리즘을 작성하라.
'''

import heapq
from typing import List


def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    heap = []
    # 키 역순, 인덱스 삽입
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))

    result = []
    # 키 역순, 인덱스 추출
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], [-person[0], person[1]])
