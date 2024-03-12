# day 2 복습
# 1 - sorting&greedy (에산)
from collections import deque
print("--------------------------------------------------")


def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget >= i:
            budget -= i
            answer += 1
        else:
            break

    return answer


# 2 - sorting&greedy (회의실 배정)
print("--------------------------------------------------")


def solution2(arr):
    answer = 0
    arr.sort(key=lambda x: (x[1], x[0]))
    end = arr[0][1]

    for i in range(len(arr)-1):
        if end <= arr[i+1][0]:
            end = arr[i+1][1]
            answer += 1

    return answer


# 3 - sorting&greedy (단속 카메라)
print("--------------------------------------------------")


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0]))

    end = routes[0][1]
    answer = 1

    for i in range(len(routes)-1):
        if end < routes[i+1][0]:  # 위 문제와 달리 등호를 뺌
            end = routes[i+1][1]
            answer += 1

    return answer


# 4 - sorting&greedy (지붕잃고 외양간 고치기)
print("--------------------------------------------------")

answer = 0
so = []
m, s, c = map(int, input().split())

for i in range(c):
    so.append(int(input()))

so.sort()

di = []

for i in range(1, len(so)):
    temp = so[i] - so[i-1]
    di.append(temp)

di.sort(reverse=True)

answer = so[-1] - so[0] + 1

for i in range(m-1):
    answer -= di[i]-1

print(answer)


# 5 - greedy (체육복)
print("--------------------------------------------------")


def solution3(n, lost, reserve):
    answer = 0

    std = [1]*(n+1)

    for i in lost:
        std[i] = 0

    reserve.sort()

    for i in reserve:
        if i in lost:
            std[i] = 1
            continue
        if i-1 >= 0 and std[i-1] == 0:
            std[i-1] = 1
            continue
        if i+1 <= n and std[i+1] == 0:
            std[i+1] = 1
            continue
    answer = std.count(1) - 1

    return answer


# 6 - stack (스택)
print("--------------------------------------------------")

stk = []
n = int(input())

for i in range(n):
    cmd = input().split()
    if cmd[0] == "i":
        stk.append(int(cmd[0]))
    elif cmd[0] == "o":
        if len(stk) == 0:
            print("empty")
        else:
            print(stk.pop())
    elif cmd[0] == "c":
        print(len(stk))

# 7 - stack (천단위 구분기호)
print("--------------------------------------------------")

n = int(input())
stk = []
n1 = input()
n1 = list(n1)
i = 1
while len(n1):
    stk.append(n1.pop())
    if i % 3 == 0 and i != n:
        stk.append(',')
    i += 1

while len(stk) > 0:
    print(stk.pop(), end='')

# 8 - stack (후위표기법)
print("--------------------------------------------------")

stk = []
n = int(input())
ex = input().split()
for i in ex:
    if i == "+":
        a = stk.pop()
        b = stk.pop()
        stk.append(b+a)
    elif i == "-":
        a = stk.pop()
        b = stk.pop()
        stk.append(b-a)
    elif i == "*":
        a = stk.pop()
        b = stk.pop()
        stk.append(b*a)
    elif i == "/":
        a = stk.pop()
        b = stk.pop()
        stk.append(int(b/a))
    else:
        stk.append(int(i))

print(stk.pop())


# 9 - queue (큐)
print("--------------------------------------------------")

q = []
n = int(input())

for i in range(n):
    cmd = input().split()
    if cmd[0] == "i":
        q.append(int(cmd[1]))
    elif cmd[0] == "o":
        if len(q) == 0:
            print("empty")
        else:
            print(q.pop(0))
    elif cmd[0] == "c":
        print(len(q))


# 10 - queue (요세푸스 순열)
print("--------------------------------------------------")


N, K = map(int, input().split())

q = [i for i in range(1, N+1)]
q = deque(q)

ans = []

idx = 0

while q:
    for i in range(K-1):
        if len(q) != 0:
            q.append(q.popleft)
    if len(q) != 0:
        ans.append(q.popleft())

print(' '.join(map(str, ans)))
