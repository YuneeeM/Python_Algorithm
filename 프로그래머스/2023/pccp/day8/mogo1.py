# 실습용 로봇
def solution(command):
    lc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    st = 0
    ed = 0
    d = 0
    command = list(command)
    for i in command:
        if i == "R":
            d = (d+1) % 4
        elif i == "L":
            d = (d-1) % 4
        elif i == "G":
            st = st + lc[d][0]
            ed = ed + lc[d][1]
        elif i == "B":
            st = st - lc[d][0]
            ed = ed - lc[d][1]

    return [st, ed]
