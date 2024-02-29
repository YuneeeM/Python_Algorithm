# 체육복
def solution2(n, lost, reserve):
    answer = 0
    # 학생 리스트
    # 인덱스의 값이 0부터 시작되기에 +1 추가하고 마지막에 -1
    std = [1]*(n+1)

    # 안가져온 학생
    for i in lost:
        std[i] = 0

    # 여유로 가져온 친구드링 오름차순으로 정렬된 데이터라는게 보장이 없다
    reserve.sort()

    for i in reserve:
        # 만약 내가 여유있게 가져왔는데 잃어버린 학생에 포함된다면 못빌려줌;;
        if i in lost:
            std[i] = 1
            continue
        # 왼쪽 친구가 잃어버린 친구인가?
        if i-1 >= 0 and std[i-1] == 0:
            std[i-1] = 1
            continue
        # 오른쪽 친구가 잃어버린 친구인가?
        if i+1 <= n and std[i+1] == 0:
            std[i+1] = 1
            continue

    answer = std.count(1) - 1

    return answer
