#홀짝 연결리스트 - 반복 구조로 홀짝 노드 처리
'''
연결리스트를 홀수 번째 노드 다음에 짝수 번째 노드가 오도록 재구성하라.
공간 복잡도 O(1), 시잔 복잡도 O(n)에 풀이하라.
'''
def oddEvenList(self, head:ListNode) -> ListNode:
  #예외처리
  if head is None:
    return None
  
  odd = head
  even = head.next
  even_head=head.next

  #반복하면서 홀짝 노드 처리
  while even and even.next:
    odd.next, even.next = odd.next.next, even.next.next
    odd, even = odd.next, even.next

  #홀수 노드의 마지막을 짝수 헤드로 연결
  odd.next = even_head
  return head