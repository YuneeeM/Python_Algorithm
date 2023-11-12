# 푸드 파이트 대회
def solution(food):
    answer = ''
    arr = []

    for i in range(1, len(food)):
        if food[i] == 1:
            continue
        else:
            answer += str(i)*(food[i]//2)
            arr.append(str(i)*(food[i]//2))

    answer += '0'
    arr.sort(reverse=True)

    for x in arr:
        answer += x

    return answer
