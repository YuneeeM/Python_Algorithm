# 주식을 사고팔기 가장 좋은 시점 2 - 그리디 알고리즘
'''
여러번의 거래로 낼 수 있는 최대 이익을 산출하라.
'''
from typing import List


def maxProfit(self, prices: List[int]) -> List:
    result = 0
    # 값이 오르는 경우 매번 그리디 계산
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            result += prices[i+1]-prices[i]

    return result
