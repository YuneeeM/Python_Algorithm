# 연속된 수의 합
def solution(num, total):
    answer = []
    mid = total//num
    a = mid - ((num - 1)//2)  # 중앙값에서 -1, +1 이런식으로 풀면됨
    b = mid+((num+2)//2)  # num이 짝수인 경우를 고려하고  range를 고려해서 오른쪽은 +2로 계산
    for x in range(a, b):
        answer.append(x)
    return answer
