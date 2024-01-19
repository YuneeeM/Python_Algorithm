# 쿠키부여-그리디알고리즘
'''
아이들에게 1개씩 쿠키를 나눠줘야 한다. 각 아이 child_i마다 그리디 팩터 gi를 갖고 있으며, 이는 아이가 만족하는 최소
크기를 말한다. 각 쿠키는 크기 si를 갖고 있으먀, si>=gi이어야 아이가 만족하며 쿠키를 받는다.
최대 몇명의 아이들에게 쿠키를 줄 수 있는지 출력하라.
'''
from typing import List


def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()

    child_i = cookie_j = 0
    # 만족하지 못할때까지 그리디 실행
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            child_i += 1
        cookie_j += 1
    return child_i
