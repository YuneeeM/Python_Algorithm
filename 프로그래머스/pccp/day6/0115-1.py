# day5 복습
# 1
import heapq
print("--------------------------------")


def solution(input_string):
    answer = ''
    temp = set()  # 외톨이 문자
    alpha = set()

    # 맨뒤 문자 비교
    input_string += ' '

    for i in range(len(input_string)-1):
        if input_string[i] != input_string[i+1]:
            if input_string[i] not in alpha:
                alpha.add(input_string[i])
            else:
                temp.add(input_string[i])

    if len(temp) == 0:
        answer = 'N'
    else:
        temp = list(temp)
        temp.sort()
        answer = ''.join(temp)

    return answer


# 2
print("--------------------------------")

answer = 0


def DFS(L, psum, ability, visit):
    global answer

    std = len(ability)
    obj = len(ability[0])

    if L == obj:
        answer = max(answer, psum)
    else:
        for i in range(std):
            if visit[i] == 0:
                visit[i] = 1
                DFS(L+1, psum+ability[i][L], ability, visit)
                visit[i] = 0


def solution2(ability):
    visit = [0 for i in range(len(ability))]

    DFS(0, 0, ability, visit)

    return answer


# 3
print("--------------------------------")


def gene(gen, n):
    if gen == 1:
        return 'Rr'

    parent = gene(gen-1, (n-1)//4+1)

    if parent == 'RR' or parent == 'rr':
        return parent

    if n % 4 == 0:
        return 'rr'
    elif n % 4 == 1:
        return 'RR'
    else:
        return 'Rr'


def solution3(queries):
    answer = []

    for i in queries:
        answer.append(gene(i[0], i[1]))


# 4
print("--------------------------------")


def solution4(program):
    answer = [0 for i in range(11)]
    program.sort(key=lambda x: (x[1], x[0]))
    d = []

    time = 0

    while program or d:
        while program and program[0][1] <= time:
            heapq.heappush(d, program.pop(0))
        if program and not d:
            heapq.heappush(d, program.pop(0))

            time = d[0][1]

        proinfo = heapq.heappop(d)
        answer[proinfo[0]] += (time-proinfo[1])

        time += proinfo[2]
    answer[0] = time
    return answer
