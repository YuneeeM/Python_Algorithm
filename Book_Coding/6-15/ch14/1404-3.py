# 이진 트리 반전 - 반복구조로 DFS
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
    stack = collections.deque([root])

    while stack:
        node = stack.pop()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left

            stack.append(node.left)
            stack.append(node.right)
    return root
