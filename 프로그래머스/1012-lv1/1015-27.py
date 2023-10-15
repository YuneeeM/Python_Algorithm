# 문자열 다루기 기본
def solution(s):
    if (len(s) == 4 or len(s) == 6):
        for x in str(s):
            if x not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                return False
        return True

    return False
