# 최빈값 구하기
def solution(array):
    ch = [0]*1000

    for x in array:
        ch[x] += 1

    m = 0
    for x in ch:
        if x == max(ch):
            m += 1

    if m > 1:
        return -1
    else:
        return ch.index(max(ch))
