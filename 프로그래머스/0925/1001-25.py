# 문자열안에 문자열
def solution(str1, str2):
    if str1.find(str2) > -1:
        return 1
    else:
        return 2


def test(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2
