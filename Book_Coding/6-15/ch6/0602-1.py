#문자열 뒤집기 - 투 포인터를 이용한 swap
#입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

def reverseString(self, s:list[str]) -> None:
  left, right = 0, len(s) -1
  while left < right:
    s[left], s[right]  = s[right], s[left]
    left+=1
    right+=1