# 다음에 올 숫자
def solution(common):
    answer = 0
    arr = []

    for i in range(len(common)-1):
        arr.append(common[i+1]-common[i])

    arr = set(arr)

    if len(arr) == 1:
        arr = list(arr)
        answer = common[0]+(len(common))*arr[0]
    else:
        arr = []
        for i in range(len(common)-1):
            arr.append(common[i+1]//common[i])

        answer = common[0]*(arr[0]**(len(common)))

    return answer
