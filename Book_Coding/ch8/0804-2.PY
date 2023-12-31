#두 수의 덧셈 - 전가산기 구현
'''
역순으로 저장된 연결리스트의 숫자를 더하라
'''

def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
  root = head = ListNode(0)

  carry = 0

  while l1 or l2 or carry:
    sum = 0
    #두 입력값의 합 계산
    if l1:
      sum+=l1.val
      l1 = l1.next
    if l2:
      sum+=l2.val
      l2=l2.next

    #몫(자리올림수)과 나머지(값) 계산
    carry,val = divmod(sum+carry, 10)
    head.next = ListNode(val)
    head = head.next

  return root.next