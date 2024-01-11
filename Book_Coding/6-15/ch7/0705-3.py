#배열 파티션1 - 파이썬다운 방식
'''
n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
'''

def arrayPairSum(self, nums:list[int]) -> int:
  return sum(sorted(nums[::2]))