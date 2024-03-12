# [PCCP 모의고사 #1] 4번 - 운영체제
import heapq


def solution(program):
    answer = [0 for i in range(11)]

    program.sort(key=lambda x: (x[1], x[0]))

    # 프로그램 시간의 흐름
    time = 0

    # 대기중인 프로그램
    d = []

    # 동작시킬 프로그래밍이 있는지, 대기중인 프로그램이 있는지, 있다면 계속 동작
    while program or d:
        # 대기 중 프로그램이 있는데 실행하는게 있을 수도 있고, 없을 수도 있음
        # 현 동작중인 프로그램이 없다면(현 시간보다 앞에 시작하는 프로그램)
        while program and program[0][1] <= time:
            # d.append(program.pop(0))
            heapq.heappush(d, program.pop(0))
            # 대기 순서에 들어가면
            # 프로그램의 순서의 우선순위가 우선되어야 한다
            # d.sort()
        # 프로그램이 남았는데 대기중인 프로그램이 없다면
        # 현 동작시키고 있는 프로그램도 없음
        if program and not d:
            heapq.heappush(d, program.pop(0))
            # d.sort()
            # 대기중 맨 앞에 있는 프로그래밍의 시작시간으로 이동
            time = d[0][1]
        proinfo = heapq.heappop(d)
        # 현시간 - 프로그램 시작시간 = 대기시간
        answer[proinfo[0]] += (time - proinfo[1])
        # 프로그램을 꺼내서 보니 우선순위에 밀려날 수 있기 때문에 +=으로 누적

        # 시간의 흐름(지금 동작하고 있는 프로그램의 끝나는 시간으로 변경)
        time += proinfo[2]

    # 끝나는 시간 표시
    answer[0] = time
    return answer
