# 삽입 정렬 리스트 - 삽입 정렬
'''
연결리스트를 삽입 정렬로 정렬하라.
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


def insertionSortList(self, head: ListNode) -> ListNode:
    cur = parent = ListNode(None)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next
        cur.next, head.next, head = head, cur.next, head.next

        cur = parent
    return cur.next
