# K번째수
def solution(array, commands):
    answer = []
    for x in range(len(commands)):
        i, j, k = commands[x][0], commands[x][1], commands[x][2]
        arr = array
        arr = arr[i-1:j]
        arr.sort()
        answer.append(arr[k-1])

    return answer
