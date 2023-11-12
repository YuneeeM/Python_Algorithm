# 삼각형의 완성조건 (2)
def solution(sides):
    sides.sort()
    arr = []
    for x in range(sides[0], sides[1]+1):
        if sides[0] + x > sides[1]:
            arr.append(x)

    for x in range(sides[1]-sides[0]+1, sides[0]+sides[1]+1):
        if sides[0]+sides[1] > x:
            arr.append(x)

    result = list(set(arr))

    return len(result)
