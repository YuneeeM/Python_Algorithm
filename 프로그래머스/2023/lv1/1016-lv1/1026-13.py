# [1차] 비밀지도
def solution(n, arr1, arr2):
    answer = []
    num = ''
    arr1 = [bin(x)[2:].zfill(n) for x in arr1]
    arr2 = [bin(x)[2:].zfill(n) for x in arr2]

    for i in range(n):
        for x in range(len(arr1[i])):
            if '1' == arr1[i][x] or '1' == arr2[i][x]:
                num += '#'
            elif '0' == arr2[i][x] and '0' == arr2[i][x]:
                num += ' '
        answer.append(num)
        num = ''

    return answer
