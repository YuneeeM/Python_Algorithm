# A로 B 만들기
def solution(before, after):
    answer = 0
    for x in str(before):
        if str(before).count(x) != str(after).count(x):
            return 0
    else:
        return 1
