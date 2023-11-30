#배열 파티션1 - 짝수 번째 값 계산
'''
n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
'''
def arrayPairSum (self, nums: list[int]) -> int:
  sum=0
  nums.sort()

  for i, n in enumerate(nums):
    #짝수 번째 값의 합 계산
    if i%2 == 0:
      sum+=n

  return sum