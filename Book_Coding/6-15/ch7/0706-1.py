#자신을 제외한 배열의 곱 - 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
'''
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.
'''
def productExceptSelf (self, nums:list[int]) -> list[int]:
  out=[]
  p=1
  #왼쪽 곱셈
  for i in range(0,len(nums)):
    out.append(p)
    p=p*nums[i]
  p=1
  #왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
  for i in range(len(nums)-1,0-1,-1):
    out[i] = out[i]*p
    p=p*nums[i]
    
  return out