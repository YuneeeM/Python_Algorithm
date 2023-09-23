# 2차원으로 만들기
from collections import deque


def solution(num_list, n):
    answer = []
    a = []
    i = 0
    num_list = deque(num_list)
    while num_list:

        if i == n:
            answer.append(a)
            i = 0
            a = []
        else:
            cur = num_list.popleft()
            a.append(cur)
            i += 1
    answer.append(a)
    return answer
