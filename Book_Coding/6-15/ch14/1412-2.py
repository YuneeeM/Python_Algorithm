# 이진 탐색 트리(BST) 노드 간 최소거리 - 반복 구조로 중위 순회
'''
두 노드 간 값의 차이가 가장 작은 노드의 값의 차이를 출력하라.
'''
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDiffInBST(self, root: TreeNode) -> int:
    prev = -sys.maxsize
    result = sys.maxsize

    stack = []
    node = root

    # 반복 구조 중위 순회 비교 결과
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()

        result = min(result, node.val - prev)
        prev = node.val

        node = node.right

    return result
