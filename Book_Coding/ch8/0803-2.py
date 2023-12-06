#역순 연결리스트 - 반복 구조로 뒤집기
'''
연결리스트를 뒤집어라
'''
def reverseList(self, head: ListNode) -> ListNode:
  node, prev = head, None

  while node:
    next, node.next = node.next, prev
    prev, node = node, next
  
  return prev