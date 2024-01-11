#두 수의 합 - 두 포인터 이용
def twoSum(self, nums: list[int], target: int) -> list[int]:
  left,right = 0,len(nums)-1
  while not left == right:
    #합이 타켓 보다 작으면 왼쪽 포인터를 오른쪽으로
    if nums[left] + nums[right] < target:
      left+=1
    #합이 타켓보다 크면 오른족 포인터를 왼쪽으로
    elif nums[left]+nums[right] > target:
      right -=1
    else:
      return [left,right]