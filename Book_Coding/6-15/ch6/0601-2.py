#데크 자료형을 이용한 최적화
from collections import deque

def isPalindrome(self,s:str) -> bool:
  #자료형 데크로 선언
  strs : Deque = deque()

  for char in s:
    if char.isalnum():
      strs.append(char.lower())
      
  #팰린드롬 여부 판별
  while len(strs) > 1:
    if strs.popleft() != strs.pop():
      return False
    
  return True
