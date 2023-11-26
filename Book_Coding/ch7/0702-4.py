#두 수의 합 - 조회 구조 개선
def twoSum (self, nums: list[int], target: int) -> list[int]:
  nums_map={}
  #하나의 for 문으로 통합
  for i, num in enumerate(nums):
    if target - num in enumerate(nums):
      return [nums_map[target-num], i]
    nums_map[num] = i