#두 정렬 리스트의 병합 - 재귀 구조로 연결
'''
정렬되어 있는 두 연결리스트를 합쳐라
'''

def mergeTwoLists(self, l1:ListNode, l2: ListNode) -> ListNode:
  if (not l1) or (l2 and l1.val > l2.val):
    l1,l2 = l2, l1
  if l1:
    l1.next = self.mergeTwoLists(l1.next,l2)
  return l1