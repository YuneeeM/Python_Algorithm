#팰린드롬 연결 리스트 - 데크를 이용한 최적화
'''
연결리스트가 팰린드롬 구조인지 판별하라 ( 팰린드롬의 정의가 기억나지 않는다면 138페이지를 다시 참고하라)

'''
import collections

def isPalindrome ( self, head:ListNode) -> bool:
  #데크 자료형 선언
  q:Deque = collections.deque()

  if not head:
    return True
  
  node = head

  #리스트 변환
  while node is not None:
    q.append(node.val)
    node=node.next

  #팰린드롬 판별
  while len(q) > 1:
    if q.popleft() != q.pop():
      return False
  return True