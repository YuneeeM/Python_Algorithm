# 명예의 전당 (1)
def solution(k, score):
    answer = []
    arr = []
    for i in range(len(score)):
        if len(arr) < k:
            arr.append(score[i])
            arr.sort(reverse=True)
        elif len(arr) == k:
            if score[i] > arr[-1]:
                arr.pop()
                arr.append(score[i])
                arr.sort(reverse=True)

        answer.append(arr[-1])
    return answer
