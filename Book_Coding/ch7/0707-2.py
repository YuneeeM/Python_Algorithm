import sys
#주식을 사고팔기 가장 좋은 시점 - 저점과 현재 값과의 차이 계산
'''
한 번의 거래로 낼 수 있는 최대 이익을 산출하라
'''
def maxProfit(self, prices:list[int]) -> int:
  profit=0
  min_price = sys.maxsize

  #최솟값과 최댓값을 계속 갱신
  for price in prices:
    min_price = min(min_price,price)
    profit = max(profit,price-min_price)

  return profit