# 이진 탐색 트리(BST) 합의 범위 - 반복 구조 BFS로 필요한 노드 탐색
'''
이진 탐색 트리(BST)가 주어졌을 때 L이상 R이하의 값을 지닌 노드의 합을 구하라.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    stack, sum = [root], 0
    # 큐 연산을 이용해 반복 구조 BFS로 필요한 노드 탐색
    while stack:
        node = stack.pop(0)
        if node:
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
            if L <= node.val <= R:
                sum += node.val
    return sum
