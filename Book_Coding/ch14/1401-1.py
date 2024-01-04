# 이진트리의 최대 깊이 - 반복 구조로 BFS 풀이
'''
이진트리의 최대 깊이를 구하라
'''
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    queue = collections.deque([root])  # BFS 탐색을 위한 초기화
    depth = 0

    while queue:
        depth += 1
        # 큐 연산 추출 노드의 자식 노드 삽입
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
    # BFS 반복횟수 == 깊이
    return depth
