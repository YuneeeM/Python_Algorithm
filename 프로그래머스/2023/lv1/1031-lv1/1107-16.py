#햄버거 만들기
def solution(ingredient):
    answer = 0
    res = []

    for x in ingredient:
        res.append(x)
        while len(res) >= 4 and res[-4:] == [1, 2, 3, 1]:
            res.pop()
            res.pop()
            res.pop()
            res.pop()
            answer += 1

    return answer
