# 카페 확장
from collections import deque


def solution(menu, order, k):
    answer = 0
    q = deque()
    complete = -1
    idx = 0
    for t in range(k*(len(order)-1)+1):
        if t == complete:
            q.popleft()
            complete = -1
        if t == k*idx:
            q.append(order[idx])
            idx += 1
        if complete == -1 and len(q) > 0:
            complete = t+menu[q[0]]

        answer = max(answer, len(q))

    return answer
