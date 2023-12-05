#역순 연결리스트 - 재귀 구조로 뒤집기
'''
연결리스트를 뒤집어라
'''
def reverseList(self, head:ListNode) -> ListNode:
  def reverse(node: ListNode, prev : ListNode = None):
    if not node:
      return prev
    next, node.next = node.next, prev
    return reverse(next,node)
  
  return reverse(head)