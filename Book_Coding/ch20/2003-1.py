# 가장 긴 반복 문자 대체 - 투 포인터, 슬라이딩 윈도우, Counter를 모두 이용
'''
대문자로 구성된 문자열 s가 주어졌을 때 k번만큼의 변경으로 만들 수 있는, 연속으로
반복된 문자열의 가장 긴 길이를 출력하라.
'''
import collections


def characterReplacement(self, s: str, k: int) -> int:
    left = right = 0
    counts = collections.Counter()
    for right in range(1, len(s)+1):
        counts[s[right-1]] += 1
        # 가장 흔하게 등장하는 문자 탐색
        max_char_n = counts.most_common(1)[0][1]

        # k 초과시 왼쪽 포인터 이동
        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1
    return right-left
