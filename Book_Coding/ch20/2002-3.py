# 부분 문자열이 포함된 최소 윈도우 - Counter로 좀 더 편리한 풀이
'''
문자열 S와 T를 입력받아 O(n)에 T의 모든 문자가 포함된 S의 최소 윈도우를 찾아라
'''

from typing import List
import collections


def minWindow(self, s: str, t: str) -> str:
    t_count = collections.Counter(t)
    current_count = collections.Counter()

    start = float('-inf')
    end = float('inf')

    left = 0

    # 오른쪽 포인터 이동
    for right, char in enumerate(s, 1):
        current_count[char] += 1

        # AND 연산 결과로 왼쪽 포인터 이동 판단
        while current_count & t_count == t_count:
            if right - left < end-start:
                start, end = left, right
            current_count[s[left]] -= 1
            left += 1

    return s[start:end] if end-start <= len(s) else ''
