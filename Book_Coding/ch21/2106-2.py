# 쿠키부여 - 이진 검색
'''
아이들에게 1개씩 쿠키를 나눠줘야 한다. 각 아이 child_i마다 그리디 팩터 gi를 갖고 있으며, 이는 아이가 만족하는 최소
크기를 말한다. 각 쿠키는 크기 si를 갖고 있으먀, si>=gi이어야 아이가 만족하며 쿠키를 받는다.
최대 몇명의 아이들에게 쿠키를 줄 수 있는지 출력하라.
'''
import bisect
from typing import List


def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()

    result = 0
    for i in s:
        # 이진 검색으로 더 큰 인덱스 탐색
        index = bisect.bisect_right(g, i)
        if index > result:
            result += 1
    return result
