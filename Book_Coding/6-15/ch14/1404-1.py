# 이진 트리 반전 - 파이썬다운 방식
'''
중앙을 기준으로 이진 트리 반전하기
'''

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(self, root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = self.invertTree(
            root.right), self.invertTree(root.left)
        return root
    return None
