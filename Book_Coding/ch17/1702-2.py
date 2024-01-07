# 리스트 정렬 - 내장함수를 이용하는 실용적인 방법
'''
연결리스트를 O(nlogn)에 정렬하라.
'''


from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


def sortList(self, head: ListNode) -> ListNode:
    # 연결 리스트 -> 파이썬 리스트
    p = head
    lst: List = []
    while p:
        lst.append(p.val)
        p = p.next

    # 정렬
    lst.sort()

    # 파이썬 리스트 -> 연결 리스트
    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next

    return head
