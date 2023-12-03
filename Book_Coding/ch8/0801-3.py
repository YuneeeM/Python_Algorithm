#팰린드롬 연결 리스트 - 런너를 이용한 우아한 풀이
'''
연결리스트가 팰린드롬 구조인지 판별하라 ( 팰린드롬의 정의가 기억나지 않는다면 138페이지를 다시 참고하라)
'''
def isPalindrome(self,head:ListNode) -> bool:
  rev=None
  slow=fast=None
  #런너를 이용해 역순 연결 리스트 구성
  while fast and fast.next:
    fast=fast.next.next
    rev, rev.next , slow = slow, rev, slow.next
  if fast:
    slow = slow.next

  #팰린드롬 여부 확인
  while rev and rev.val == slow.val:
    slow, rev = slow.next, rev.next  
  return not rev