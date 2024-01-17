# 신입사원 교육
import heapq


def solution(ability, number):
    answer = 0
    ability.sort()
    for _ in range(number):
        a = heapq.heappop(ability)
        b = heapq.heappop(ability)
        heapq.heappush(ability, a+b)
        heapq.heappush(ability, a+b)

    return sum(ability)
