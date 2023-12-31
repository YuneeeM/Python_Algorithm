# 이진트리의 직경 - 상태값 누적 트리 DFS
'''
이진 트리에서 두 노드 간 가장 긴 경로의 길이를 출력하라
'''
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left+right+2)
            # 상태값
            return max(left, right)+1
        dfs(root)
        return self.longest
