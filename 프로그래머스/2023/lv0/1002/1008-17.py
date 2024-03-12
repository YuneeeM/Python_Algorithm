# 특이한 정렬

def custom_sort(item):
    return (item[0], -item[1])


def solution(numlist, n):
    answer = []
    arr = []
    num = 0
    numlist.sort(reverse=True)
    for x in numlist:
        num = abs(x-n)
        answer.append([num, x])

    answer = sorted(answer, key=custom_sort)
    for a, b in answer:
        arr.append(b)
    return arr
