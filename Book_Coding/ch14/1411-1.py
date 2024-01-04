# 이진 탐색 트리(BST) 합의 범위 - 재귀 구조 DFS로 브루트 포스 탐색
'''
이진 탐색 트리(BST)가 주어졌을 때 L이상 R이하의 값을 지닌 노드의 합을 구하라.
'''

import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    if not root:
        return 0

    return (root.val if L <= root.val <= R else 0) + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
