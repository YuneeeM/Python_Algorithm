# 이진 검색 - 이진 검색을 사용하지 않는 index 풀이

'''
정렬된 nums를 입력받아 이진 검색으로 target에 해당하는 인덱스를 찾아라.

'''

from typing import List


def search(self, nums: List[int], target: int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1
