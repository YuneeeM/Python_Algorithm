# 부분 문자열이 포함된 최소 윈도우 - 모든 윈도우 크기를 브루트 포스로 탐색
'''
문자열 S와 T를 입력받아 O(n)에 T의 모든 문자가 포함된 S의 최소 윈도우를 찾아라
'''

from typing import List


def minWindow(self, s: str, t: str) -> str:
    def contains(s_substr_lst: List, t_lst: List):
        for t_elem in t_lst:
            if t_elem in s_substr_lst:
                s_substr_lst.remove(t_elem)
            else:
                return False
        return True

    if not s or not t:
        return ''

    window_size = len(t)

    for size in range(window_size, len(s)+1):
        for left in range(len(s)-size+1):
            s_substr = s[left:left+size]
            if contains(list(s_substr), list(t)):
                return s_substr
    return ''
