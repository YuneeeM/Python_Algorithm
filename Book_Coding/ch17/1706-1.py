# 유효한 애너그램
'''
t가 s의 애너그램인지 판별하라
'''


def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
