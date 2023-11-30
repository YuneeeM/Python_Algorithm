#주식을 사고팔기 가장 좋은 시점 - 브루트 포스로 계산
'''
한 번의 거래로 낼 수 있는 최대 이익을 산출하라
'''

def maxProfit(self, prices: list[int]) -> int:
  max_price=0

  for i, price in enumerate(prices):
    for j in range(i,len(prices)):
      max_price = max(prices[j] - price , max_price)
  
  return max_price
