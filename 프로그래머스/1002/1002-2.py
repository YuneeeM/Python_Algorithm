# 잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    my_str = [x for x in my_str]

    count = 0
    res = ""

    for x in my_str:
        res += x
        count += 1
        if count == n:
            count = 0
            answer.append(res)
            res = ""
    if len(res) > 0:
        answer.append(res)

    return answer
