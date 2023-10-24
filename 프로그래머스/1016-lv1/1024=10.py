# 가장 가까운 같은 글자
def solution(s):
    answer = []
    arr = []

    for i in range(len(s)):
        if s[i] in arr:
            answer.append(i-arr.index(s[i]))
            arr[arr.index(s[i])] = "-1"
        else:
            answer.append(-1)

        arr.append(s[i])

    return answer
