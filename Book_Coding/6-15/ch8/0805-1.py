#페어의 노드 스왑 - 값만 교환
'''
연결리스트를 입력받아 페어 단위로 스왑하라
'''

def swapPairs(self, head:ListNode) -> ListNode:
  cur=head

  while cur and cur.next:
    #값만 교환
    cur.val, cur.next.val = cur.next.val, cur.val
    cur = cur.next.next
    
  return head