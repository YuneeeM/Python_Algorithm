# 회의실 배정
def solution(arr):
    arr.sort(key=lambda x: (x[1], x[0]))
    et = 0  # 회의 끝나는 시간
    cnt = 0
    for s, e in arr:
        if s >= et:
            et = e
            cnt += 1
    return cnt


def solution2(arr):
    answer = 0
    # 가장 빨리 띁나는 회의 순 ...
    # 끝나는게 같다면 시작이 빠른 순
    arr.sort(key=lambda x: (x[1], x[0]))

    # 처음 회의실 사용팀 끝나는 시간 기억
    end = arr[0][1]
    # 처음 회의실 사용팀 수
    answer = 1
    # 전체팀 -1 수 만큼 비교
    for i in range(len(arr)-1):
        # 끝나는 시간보다 시작 시간이 이상입니까?
        if end <= arr[i+1][0]:
            # 끝나는 시간 갱신
            end = arr[i+1][1]
            answer += 1

    return answer
