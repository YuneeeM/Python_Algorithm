# 두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] in answer:
                continue
            answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer
