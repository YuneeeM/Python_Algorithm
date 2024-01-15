# 주식을 사고팔기 가장 좋은 시점 2 - 파이썬 다운 방식
'''
여러번의 거래로 낼 수 있는 최대 이익을 산출하라.
'''
from typing import List


def maxProfit(self, prices: List[int]) -> List:
    # 0보다 크면 무조건 합산
    return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))
