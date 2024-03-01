# 최소직사각형
def solution(sizes):
    answer = 0
    n = len(sizes)
    a = []
    b = []
    for i in range(n):
        if sizes[i][0] >= sizes[i][1]:
            a.append(sizes[i][0])
            b.append(sizes[i][1])
        else:
            b.append(sizes[i][0])
            a.append(sizes[i][1])
    answer = max(a) * max(b)

    return answer
