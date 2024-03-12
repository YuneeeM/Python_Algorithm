# 체육복
def solution(n, lost, reserve):
    reserve.sort()
    lost.sort()

    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    # 앞번호와 뒷번호 친구 삭제
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)

    return n-len(lost)


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


std = []
n = 5
for i in range(n):
    std.append(0)

std2 = [0] * n  # 일차원은 되지만 이차원은 권하지 않는다!
std2[3] = 99
print(std2)

std22 = [[0]*n]*n
std22[0][2] = 99
print(std22)  # 주소값 저장을 인한 복사 개념

std3 = [[1]*n for i in range(n)]
print(std3)

std4 = [[0 for i in range(3)] for j in range(5)]
std4[0][2] = 99
print(std4)  # 이게 원하는것
