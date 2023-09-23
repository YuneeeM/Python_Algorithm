# 공 던지기
from collections import deque


def solution(numbers, k):
    answer = 0
    numbers = deque(numbers)
    for i in range(k):
        if i == 0:
            answer = numbers.popleft()
            numbers.append(answer)
        else:
            cur1 = numbers.popleft()
            cur2 = numbers.popleft()
            numbers.append(cur1)
            numbers.append(cur2)
            answer = cur2

    return answer
