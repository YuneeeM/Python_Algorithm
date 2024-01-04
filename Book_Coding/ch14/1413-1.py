# 전위, 중위 순회 결과로 이진 트리 구축 - 전위 순회 결과로 중위 순회 분할 정복
'''
트리의 전위, 중위, 순회 결과를 입력값으로 받아 이진트리를 구축하라
'''

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if inorder:
        # 전위 순회 결과는 중위 순회 분할 인덱스
        index = inorder.index(preorder.pop(0))

        # 중위 순회 결과 분할 정복
        node = TreeNode(inorder[index])
        node.left = self.buildTree(preorder, inorder[0:index])
        node.right = self.buildTree(preorder, inorder[index+1:])

        return node
