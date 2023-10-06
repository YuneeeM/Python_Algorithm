# 유한소수 판별하기
def solution(a, b):
    bb = b
    while b:
        a, b = b, a % b
    bb = bb//a
    while bb % 2 == 0:
        bb = bb//2
    while bb % 5 == 0:
        bb = bb//5
    if bb == 1:
        return 1
    else:
        return 2
