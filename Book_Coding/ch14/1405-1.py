# 두 이진 트리 병합 - 재귀 탐색
'''
두 이진 트리를 병합하라. 중복되는 노드는 값을 합산한다.
'''

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)

        return node
    else:
        return t1 or t2
