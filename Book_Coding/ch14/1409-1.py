# 정렬된 배열의 이진 탐색 트리 변환 - 이진 검색 결과로 트리 구성
'''
오름차순으로 정렬된 배열을 높이 균형 이진 탐색 트리로 변환하라.
'''

import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if not nums:
        return None

    mid = len(nums) // 2

    # 분할 정복으로 이진 검색 트리 구성
    node = TreeNode(nums[mid])
    node.left = self.sortedArrayToBST(nums[:mid])
    node.right = self.sortedArrayToBST(nums[mid+1:])

    return node
