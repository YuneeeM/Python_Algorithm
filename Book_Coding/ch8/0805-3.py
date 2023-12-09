#페어의 노드 스왑 - 재귀 구조로 스왑
'''
연결리스트를 입력받아 페어 단위로 스왑하라
'''

def swapPairs(self, head:ListNode) -> ListNode:
  if head and head.next:
    p=head.next
    #스왑된 값 리턴 받음
    head.next=self.swapPairs(p.next)
    p.next=head
    return p 
  return head
