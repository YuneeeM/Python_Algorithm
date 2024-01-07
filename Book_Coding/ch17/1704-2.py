# 삽입 정렬의 비교 조건 개선
'''
연결리스트를 삽입 정렬로 정렬하라.
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


def insertionSortList(self, head: ListNode) -> ListNode:
    # 초깃값 변경
    cur = parent = ListNode(0)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next
        cur.next, head.next, head = head, cur.next, head.next

        # 필요한 경우에만 cur 포인터가 되돌아가도록 처리
        if head and cur.val > head.val:
            cur = parent
    return parent.next
